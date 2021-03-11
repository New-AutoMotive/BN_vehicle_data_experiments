# NB INSERT API KEY AT LINE 26

import requests
import json
import pandas as pd
import numpy as np
import csv
from datetime import datetime

# Open vrn.csv and take the vrns as a list
vrn_list = []

with open('VRN.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
    for item in data:
        vrn_list.append(item[0])
        
vrn_list=vrn_list[1:]
#print(vrn_list)

# Create a function to query the VES API with each vrn
def car_deets(reg):
    url = 'https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles'
    payload = "{\n\t\"registrationNumber\": \"%s\"\n}" % reg
    headers = {'x-api-key': #insert API key #'',
           'Content-Type': 'application/json'}
    r = requests.request("POST", url, headers = headers, data=payload)
    car = r.json()
    return car

# create a dictionary to contain our car data
car_dict = {}

#measure how fast:
now = datetime.now().time()
print('Started pinging VES API: ', now)

for reg in vrn_list:
    car_dict[reg] = car_deets(reg)

with open('result.json', 'w') as f:
    json.dump(car_dict, f)

now_n = datetime.now().time()
print('Finished pinging VES API: ', now_n)
# duration = now - now_n
# print('Elapsed time: ', duration.total_seconds())
print('Number of VRNs pinged: ', len(vrn_list))