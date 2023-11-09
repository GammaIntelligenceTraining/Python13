import requests
from bs4 import BeautifulSoup as BS
import csv

url = 'https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/oopaevaandmed/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

response = requests.get(url, headers=headers)
soup = BS(response.content, 'html.parser')

table_data = soup.find('tbody').find_all('tr')


with open('weather.csv', 'w', encoding='cp1252') as weather_file:
    csv_writer = csv.writer(weather_file, lineterminator='\n')
    for row in table_data:
        row_data = []
        for cell in row.find_all('td'):
            row_data.append(cell.text)
        csv_writer.writerow(row_data)
