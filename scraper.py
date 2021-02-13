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
# votes = soup.select('.score')
# we need the links and votes

# print(links)
# print(votes)



def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse=True) # sort by votes

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText() # can be item.getText()
        href = links[idx].get('href', None) # we want to get the attribute; # can be item.getText()
        vote = subtext[idx].select('.score')
        if len(vote): # runs if the vote "list" exists
            points = int(vote[0].getText().replace(' points', ''))
            # print(points)
            if points > 99:
                hn.append({'title': title, 'link':href, 'votes': points}) # we grabbed the link and the title
        
    return sort_stories_by_votes(hn)

# create_custom_hn(links, subtext)
# print(create_custom_hn(links, subtext))
pprint.pprint(create_custom_hn(links, subtext))
 
