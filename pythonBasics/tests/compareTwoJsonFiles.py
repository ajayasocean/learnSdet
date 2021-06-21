# Compare two Json Schemas using Python Dictionaries with example
import json

with open("../config/sampleJson.json") as cmpFile1:
    dataSampleJson = json.load(cmpFile1)
    # print(dataSampleJson)
with open("../config/2sampleJson.json") as cmpFile2:
    data2SampleJson = json.load(cmpFile2)
    # print(data2SampleJson)
    assert data2SampleJson == dataSampleJson
    if data2SampleJson == dataSampleJson:
        print('Both json files are same')
    else:
        print('Used json files are not same.')
