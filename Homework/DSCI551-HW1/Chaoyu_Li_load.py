'''
Chaoyu Li
chaoyuli@usc.edu
1/26/2022
'''

import sys
import json
import requests
import pandas as pd
import urllib.parse

CSV_NAME = "WA_Fn-UseC_-Telco-Customer-Churn.csv"
baseURL = 'https://dsci551-hw1-89e4f-default-rtdb.firebaseio.com/'


def load_content_from_csv(path):
	# load data from csv file into json format
	dataFrame = pd.read_csv(path, low_memory=False)
	dataFrame = dataFrame[dataFrame['SeniorCitizen']==1]
	json_str = dataFrame.to_json(orient='records')
	json_list = json.loads(json_str)
	return json_list

def truncate_db(url):
	try:
		delResponse = requests.delete(url + '.json')
		if delResponse.status_code == 200:
			print("Truncate firebase Successfully")
		else:
			print("Truncate DB failed, Reason: {}".format(delResponse.text))
	except:
		print("Truncate DB failed")

def upload_data(url, data):
	try:
		putResponse = requests.put(url + '.json', data)
		if putResponse.status_code == 200:
			print("Upload data Successfully")
		else:
			print("Upload data failed, Reason: {}".format(putResponse.text))
	except:
		print("Upload data failed")

def encode(str):
	return urllib.parse.quote(str, safe='').replace('.', '%2e')

def create_index(data):
	result = {}
	result_dic = {}
	index = 0
	for customer in data:
		result_dic[str(index)] = customer
		index = index + 1
	result["customers"] = result_dic
	return result


def query_data(path):
	getURL = baseURL + '/' + path + '.json'
	response = requests.get(getURL)
	return json.loads(response.text)


if __name__ == "__main__":
	filePath = './' + CSV_NAME
	fileContent = load_content_from_csv(filePath)
	fileContent_list = list(fileContent)
	print(fileContent_list)
	data = create_index(fileContent)
	print(data)
	data_str = json.dumps(data)
	#with open('./result.json', 'w') as f:
	#	json.dump(fileContent, f)
	truncate_db(baseURL)
	upload_data(baseURL, data_str)

	#jsonData = query_data("customers")
	#print(jsonData)