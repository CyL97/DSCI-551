'''
Chaoyu Li
chaoyuli@usc.edu
1/26/2022
'''

import sys
import requests

baseURL = 'https://dsci551-hw1-89e4f-default-rtdb.firebaseio.com/'

def query_data(path):
    getURL = baseURL + '/' + path + '.json'
    response = requests.get(getURL + '?orderBy="Churn"&equalTo="Yes"&print=pretty')
    return response.json()

if __name__ == '__main__':
    #print(sys.argv[1])
    fileContent = query_data("customers")
    #print(fileContent)
    #for keys,values in fileContent.items():
    #    print(values["customerID"])
    result = sorted(fileContent.items(), key=lambda item:item[1]["customerID"])
    #print(result)
    for i in range(int(sys.argv[1])):
        print(result[i][1]["customerID"])