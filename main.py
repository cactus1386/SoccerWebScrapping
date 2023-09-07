import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.skysports.com/football-results'

r = requests.get(url)

if r.status_code == 200:
    content = r.text
else:
    print('failed to retrieve webpage.')


soup = BeautifulSoup(content, 'html.parser')
results = []
result_elements = soup.find_all('div', class_='fixres__item')

for element in result_elements:
    home_team = element.find('span', class_='matches__participant--side1').text
    match_score = element.find('span', class_='matches__teamscores').text
    away_team = element.find('span', class_='matches__participant--side2').text

    home = re.sub(r'\s+', ' ', home_team)
    score = re.sub(r'\s+', '  ', match_score)
    away = re.sub(r'\s+', ' ', away_team)


    results.append(f'{home} {score} {away}')

for result in results:
    print(result + '\n')