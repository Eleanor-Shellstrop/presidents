from pprint import pprint
from bs4 import BeautifulSoup
import requests
import pandas as pd
import pprint

election = []

user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.37"
URL = "https://en.wikipedia.org/wiki/List_of_United_States_presidential_elections_by_popular_vote_margin"
response = requests.get(URL, headers={'User-Agent': user_agent})
html = response.content
soup = BeautifulSoup(html, "lxml")

for tr in soup.find_all('tr'):
		data = []
		for td in tr:
			clean_text = td.get_text().strip('\n')
			if len(clean_text) < 1:
				continue
			if clean_text == ',No candidate[a]':
				clean_text = 'No Candidate, ' + ', '
			data.append(clean_text)
		if (data == []) or (len(data) < 10):
			continue
		election.append(data)


# pprint.pprint(election)
df = pd.DataFrame(election, columns = [
	'election_number', 'year', 'winner', 
	'party', 'number_electoral_votes', 'electoral_perc', 
	'pop_vote_perc', 'pop_margin_perc', 'number_pop_votes',
	'number_pop_margin', 'runner_up_name', 'runner_up_party', 'turnout_perc']) 
df.to_csv(f'../datasets/elections.csv', sep=',', encoding='utf-8-sig', index = False)