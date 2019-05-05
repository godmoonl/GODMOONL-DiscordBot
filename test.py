from urllib.request import urlopen
from urllib.request import HTTPError
import urllib.request
from bs4 import BeautifulSoup

def wiki(message):
    location = urllib.parse.quote(message)

    url = 'https://ko.wikipedia.org/wiki/'+ location
    try:
        html = urlopen(url)
    except HTTPError:
        return 0
    soup = BeautifulSoup(html,'html.parser')
    ans = soup.find('div', class_='mw-parser-output').find('p').text
    return ans+'\n'+url
def namu(message):
    location = urllib.parse.quote(message)
    url = 'https://namu.wiki/w/'+location
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url,headers=hdr)
    response = urlopen(req)
    soup = BeautifulSoup(response,'html.parser')
    ans = soup.find('div',class_='wiki-heading-content').text[:500]
    return ans+'...\n'+url

def enwiki(message):
    location = urllib.parse.quote(message)
    url = 'https://en.wikipedia.org/wiki/'+ location
    try:
        html = urlopen(url)
    except HTTPError:
        return 0
    soup = BeautifulSoup(html,'html.parser')
    ans = soup.find('div', class_='mw-parser-output').find('p').text
    return ans+'\n'+url  
class Weather:
    def __init__(self,message):
        location = urllib.parse.quote(message+'+날씨')
        url = 'https://search.naver.com/search.naver?ie=utf8&query='+ location
        html = urlopen(url)
        soup = BeautifulSoup(html,'html.parser')
        self.temp = soup.find('span', class_='todaytemp').text
        aq = soup.find('dl',class_='indicator').text.split(' ')
        self.aq = aq
        aqt = aq[2].split('㎍/㎥')[1]
        if aqt == '좋음':
            c = 0x32a1ff
        elif aqt == '보통':
            c = 0x00a83d
        elif aqt == '나쁨':
            c = 0xfd9b5a
        else:
            c = 0xff5959
        self.color = c
        
class Melon:
    def __init__(self):
        url = 'http://www.melon.com/chart/index.htm'
        hdr = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url,headers=hdr)
        response = urlopen(req)
        soup = BeautifulSoup(response,'html.parser')
        tag = []
        a = []
        for t in soup.find_all('tr',class_='lst50'):
            tag.extend(t.find('div',class_='wrap_song_info').find_all('a')[:1])
            a.extend(t.find('div',class_='wrap_song_info').find_all('a')[2:])
        if __name__ == "__main__":
            for i in range(50):
                print(i+1,tag[i].text,a[i].text)
        self.tag=tag
        self.a=a
if __name__ == "__main__":
    Melon()
