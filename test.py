from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup

def wiki(message):
    location = urllib.parse.quote(message)

    url = 'https://ko.wikipedia.org/wiki/'+ location
    html = urlopen(url)
    soup = BeautifulSoup(html,'html.parser')
    ans = soup.find('div', class_='mw-content-ltr').find('p').text
    if not ans:
        print('오류')
    else: 
        return ans+'\n'+url