from urllib.request import urlopen
from urllib.request import HTTPError
import urllib
from bs4 import BeautifulSoup

def wiki(message):
    location = urllib.parse.quote(message)

    url = 'https://ko.wikipedia.org/wiki/'+ location
    try:
        html = urlopen(url)
    except HTTPError as e:
        return 0
    soup = BeautifulSoup(html,'html.parser')
    ans = soup.find('div', class_='mw-parser-output').find('p').text
    return ans+'\n'+url
def enwiki(message):
    location = urllib.parse.quote(message)
    url = 'https://en.wikipedia.org/wiki/'+ location
    try:
        html = urlopen(url)
    except HTTPError as e:
        return 0
    soup = BeautifulSoup(html,'html.parser')
    ans = soup.find('div', class_='mw-parser-output').find('p').text
    print(ans)
    return ans+'\n'+url  

def weather(message):
    location = urllib.parse.quote(message+'+날씨')
    url = 'https://search.naver.com/search.naver?ie=utf8&query='+ location
    try:
        html = urlopen(url)
    except HTTPError as e:
        return 0
    soup = BeautifulSoup(html,'html.parser')
    ans = soup.find('div', class_='info_data').find('p',class_='info_temperature').text+'\n'+soup.find('div',class_='detail_box').text
    return ans 
