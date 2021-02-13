'''
Grabs the link of the story that has more than 100 votes
'''

import requests # allows us to download initially the html
from bs4 import BeautifulSoup # use the html to scrape; cleans up the data
import pprint

response = requests.get('https://news.ycombinator.com/news')
# print(response.text)

# CSS selector allows us to grab elements in a HTMl page
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext') 

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True) # sort by votes

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText() # can be links[idx].getText()
        href = item.get('href', None) # we want to get the attribute; # can be links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote): # runs if the vote "list" exists
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link':href, 'votes': points}) # we grabbed the link and the title
        
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))
 
