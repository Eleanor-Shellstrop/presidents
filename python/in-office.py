from bs4 import BeautifulSoup
import requests
import pandas as pd


office = []

user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.37"
URL = "https://millercenter.org/president"
response = requests.get(URL, headers={'User-Agent': user_agent})
html = response.content
soup = BeautifulSoup(html, "lxml")

for x in soup.find_all('div', attrs={'class': 'info-wrapper'}):
	name = x.find("a").get_text(strip=True)
	year_start = x.find(class_="views-field--inauguration-date").get_text(strip=True)
	year_end = x.find(class_="views-field--date-ended").get_text(strip=True)
	office.append([name, year_start, year_end])

df = pd.DataFrame(office, columns = ['name', 'start', 'end']) 
df.to_csv(f'../datasets/in-office.csv', sep=',', encoding='utf-8-sig', index = False)