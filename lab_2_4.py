import boto3
import pandas as pd
from io import StringIO

s3 = boto3.resource('s3', region_name='us-east-1')

bucket = s3.Bucket('lab-2-andrew')
files = bucket.objects.all()

name = input('Enter name file - ')

for file in files:
    if file.key == f'{name}.csv':
        file_content = file.get()['Body'].read().decode('utf-8')
        df = pd.read_csv(StringIO(file_content), usecols=['exchangedate', 'cc','rate'])
        print(df.to_string(max_rows=None))