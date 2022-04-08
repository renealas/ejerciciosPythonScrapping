import requests
from bs4 import BeautifulSoup
import csv

headers = {'Accept-Language': 'en-US'}
# website = requests.get('https://www.imdb.com/', headers=headers)
# soup = BeautifulSoup(website.text, 'html.parser')

# #featured_movie_data = soup.select('.ipc-shoveler')

# print(soup.select('.ipc-sub-grid'))

website = requests.get('https://www.imdb.com/title/tt0770828/', headers=headers)
soup = BeautifulSoup(website.text, 'html.parser')

title = soup.select_one('.sc-94726ce4-1 > h1')
runtime = soup.select('.ipc-inline-list > li')[2].text
plot = soup.select_one('.sc-16ede01-8 > p').text
rating = soup.select_one('.sc-7ab21ed2-2').text
raitingcount = soup.select_one('.sc-7ab21ed2-3').text

castData = soup.select('.sc-11eed019-7')[:5]

cast = ''

for actor in castData:
    #image = cast.select_one('.ipc-media > img').attrs['src']
    actorname = actor.select_one('.sc-11eed019-1').text
    #character = cast.select_one('.sc-11eed019-5').text
    cast += actorname + ', '

print(cast[:-2])