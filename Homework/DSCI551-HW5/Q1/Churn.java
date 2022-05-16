/**
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
//package org.apache.hadoop.examples;

import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

public class Churn {

  public static class TokenizerMapper 
       extends Mapper<Object, Text, Text, IntWritable>{
    
    private IntWritable outputValue = new IntWritable();
    private Text  outputKey = new Text();
      
    public void map(Object key, Text value, Context context
                    ) throws IOException, InterruptedException {

	String[] toks = value.toString().split(",");

	// hint: length of array toks: toks.length

	// hint: convert string into integer
	//      int a = Integer.parseInt("125")

	// hint: map function outputs:
	//      context.write(outputKey, outputValue);
	//System.out.print(toks[toks.length - 1]);
	if (toks[toks.length - 1].equals("Yes")) {
	        //System.out.print("!!!!!");
	 	outputKey.set(toks[8]);
	        outputValue.set(Integer.parseInt(toks[5]));
	        context.write(outputKey, outputValue);
         }
    }
  }
  
  public static class IntSumReducer 
       extends Reducer<Text,IntWritable,Text, IntWritable> {
    private IntWritable outputValue = new IntWritable();

    public void reduce(Text key, Iterable<IntWritable> values, 
                       Context context
                       ) throws IOException, InterruptedException {

	//hint: finding max of two values
	//    maxValue = Math.max(x, y) 


	int maxValue = -1,sum = 0;
	for (IntWritable val : values) {
	  maxValue = Math.max(maxValue, val.get());
	  sum += 1;
	}
	if (sum > 200) {
	  //System.out.print("1. print ");
	  outputValue.set(maxValue);
	  context.write(key, outputValue);
	}
    }
  }

  public static void main(String[] args) throws Exception {
      Configuration conf = new Configuration();
      String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
      if (otherArgs.length < 2) {
	  System.err.println("Usage: churn <in> [<in>...] <out>");
	  System.exit(2);
      }
      Job job = Job.getInstance(conf, "churn");
      job.setJarByClass(Churn.class);
      job.setMapperClass(TokenizerMapper.class);
      //job.setCombinerClass(IntSumReducer.class);
      job.setReducerClass(IntSumReducer.class);
      job.setOutputKeyClass(Text.class);
      job.setOutputValueClass(IntWritable.class);

      for (int i = 0; i < otherArgs.length - 1; ++i) {
	  FileInputFormat.addInputPath(job, new Path(otherArgs[i]));
      }
      FileOutputFormat.setOutputPath(job,
				     new Path(otherArgs[otherArgs.length - 1]));
      System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}
