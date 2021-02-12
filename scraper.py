'''
Grabs the link of the story that has more than 100 votes
'''

import requests # allows us to download initially the html
from bs4 import BeautifulSoup # use the html to scrape; cleans up the data

response = requests.get('https://news.ycombinator.com/news')
# print(response.text)

# CSS selector allows us to grab elements in a HTMl page
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.select('.storylink')
votes = soup.select('.score')
# we need the links and votes

# print(links)
# print(votes)

def create_custom_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href')
        hn.append(title)

    return hn

print(create_custom_hn(links, votes))
 
