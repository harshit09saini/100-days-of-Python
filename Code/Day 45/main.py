# Webscraping with BeautifulSoup

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

links_titles = soup.select('a.storylink')
links_scores = soup.select('span.score')

titles = []
scores = []
for link, score in zip(links_titles, links_scores):
    link_title = link.getText()
    link_score = int(score.getText().split(" ")[0])
    titles.append(link_title)
    scores.append(link_score)

maxx = max(scores)
index = scores.index(maxx)
print(titles[index+1])
