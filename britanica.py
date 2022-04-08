import requests
from bs4 import BeautifulSoup
import csv

website = requests.get('https://www.britannica.com/topic/list-of-philosophers-2027173')
soup = BeautifulSoup(website.text, 'html.parser')

links = soup.select('.topic-list .md-crosslink')

for link in links[:8]:
    try:
        website = requests.get(link.attrs['href'])
        soup = BeautifulSoup(website.text, 'html.parser')

        # Gets Name and Description
        name = soup.select_one('h1').text
        description = soup.select_one('.topic-identifier').text

        #Gets Sumary information
        summary = soup.select_one('.topic-paragraph').text
        imageData = soup.select_one('.card')
        try:
            image = imageData.select_one('a >img').attrs['src']
        except AttributeError as error:
            image = None

        summaryInfo = soup.select('dd')

        #Gets Birth Data
        birthData = summaryInfo[0]
        birthElements = birthData.select('.fact-item')
        try:
            birth = birthElements[0].text
        except AttributeError as error:
            birth = None
        except IndexError as error2:
            birth = None
        try:
            city = birthElements[1].text
        except AttributeError as error:
            city = None
        except IndexError as error2:
            city = None
        try:
            state = birthElements[2].text
        except AttributeError as error:
            state = None
        except IndexError as error2:
            state = None

        #Gets Death Data
        deathData = summaryInfo[1]
        deathElements = deathData.select('.fact-item')
        try:
            death = deathElements[0].text
        except AttributeError as error:
            death = None
        except IndexError as error2:
            death = None

        try:
            city = deathElements[1].text
        except AttributeError as error:
            city = None
        except IndexError as error2:
            city = None
        try:
            state = deathElements[2].text
        except AttributeError as error:
            state = None
        except IndexError as error2:
            state = None

        #Gets Subjects of Study
        try:
            studyData = summaryInfo[3]
            studyElements = studyData.select('a')
            studies = ''
            for study in studyElements:
                studies += study.text.strip() + ','
        except AttributeError as error:
            studies = None
        except IndexError as error2:
            studies = None
        print(f'{name}\n{description}\n{image}\n{summary}\n{birth}\n{death}\n{studies}')
        print('\n')
    except:
        print('Something went wrong')
    


