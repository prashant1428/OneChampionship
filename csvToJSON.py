import csv, json
from collections import OrderedDict

# Please change the csv file location as per your convinience
csvFilePath = '/Users/prashantsrivastav/Downloads/OC/data.csv' 

# Please change the JSON file location as per your convinience
jsonFilePath = '/Users/prashantsrivastav/Downloads/OC/schema.json' 

# Reading the csv file and writing the data in JSON file in ordered way using Ordered Dictionary
with open(csvFilePath) as csvFile, open(jsonFilePath, 'w') as jsonFile:
    csvReader = csv.DictReader(csvFile)
    jsonData = [OrderedDict((field, row[field]) for field in csvReader.fieldnames) for row in csvReader]
    json.dump(jsonData, jsonFile, indent=4, separators=(',', ': '))
