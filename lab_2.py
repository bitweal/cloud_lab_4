import requests
import json

currency = input("Enter currency - ")
url = f'https://bank.gov.ua/NBU_Exchange/exchange_site?start=20210101&end=20211231&valcode={currency}&sort=exchangedate&order=desc&json'

def get_data(currency):
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        with open(f'{currency}.json', 'w') as file:
            json.dump(data, file)
        return data
    else:
        print(f'Request failed with status code {response.status_code}')
        return -1

get_data(currency)