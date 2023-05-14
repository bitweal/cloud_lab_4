import json
import csv
import boto3

s3 = boto3.client('s3', region_name='us-east-1')

name = input('Enter name file - ')

with open(f'{name}.json', 'r') as file:
    data = json.load(file)

with open(f'{name}.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)

    writer.writerow(["exchangedate", "r030", "cc", "txt", "enname", "rate", "units", "rate_per_unit", "group", "calcdate"])

    for item in data:
        writer.writerow([item["exchangedate"], item["r030"], item["cc"], item["txt"], item["enname"], item["rate"],\
                        item["units"], item["rate_per_unit"], item["group"], item["calcdate"]])


bucket_name = 'lab-2-andrew'
file_name = f'{name}.csv'
local_file_name = f'{name}.csv'
s3.upload_file(local_file_name, bucket_name, file_name)