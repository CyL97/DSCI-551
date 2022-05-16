'''
Chaoyu Li
chaoyuli@usc.edu
1/26/2022
'''

import sys
import requests

baseURL = 'https://dsci551-hw1-89e4f-default-rtdb.firebaseio.com/'

def query_data(path, k):
    getURL = baseURL + '/' + path + '.json'
    response = requests.get(getURL + '?orderBy="tenure"&startAt=' + k + '&print=pretty')
    return response.json()

if __name__ == '__main__':
    #print(sys.argv[1])
    fileContent = query_data("customers", sys.argv[1])
    print(len(fileContent))