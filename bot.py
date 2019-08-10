import asyncio
import discord
import time
import random
import setting
import soup
import game

app = discord.Client()
embed=discord.Embed

token = setting.token

uptime = time.time()

a = setting.a
b = setting.b
admin ='528205968614490122'

def info():
    end = time.time()-uptime
    ut = int(end)
    min = int(ut/60)
    hour = int(min/60)
    day = str(int(hour/24))
    hour = str(hour%24)
    ut=str(ut%60)
    min=str(min%60)
    e = embed(title="갓봇 정보!", description="개발자 : GODMOONL#7059\n업타임 : "+day+"일 "+hour+"시간 "+min+"분 "+ut+"초 ", color=0x00C853)
    return e

@app.event
async def on_ready():
    print("다음으로 로그인 완료 :")
    print(app.user.name)
    print(app.user.id)
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    servers = len(app.servers)
    sum = 0
    for i in app.servers:
        sum += len(i.members)
    while True:
        await app.change_presence(game=discord.Game(name='`!도움` 이라고 해보세요!'))
        await asyncio.sleep(30)
        await app.change_presence(game=discord.Game(name=str(servers)+'개의 서버 | '+str(sum)+'명의 유저'))
        await asyncio.sleep(30)

@app.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == '!도움':
        r = open('update.txt',mode='rt',encoding = 'utf-8')
        rows = r.readlines()
        e = embed(title = '갓봇 도움!',description = '갓봇 명령어를 불러옵니다',color=0x00C853)
        for i in rows:
            e.add_field(name = i.split('/')[0],value=i.split('/')[1])
        e.set_footer(text='개발자 : GODMOONL#7059')
        await app.send_message(message.channel,embed=e)

    if message.content.startswith('!공지 '):
        m = message.content[4:]
        if message.author.id == admin:
            for servers in app.servers:
                print('\n'+servers.name)
                for channel in servers.channels:
                    if channel.name.find('공지') != -1 or channel.name.find('notice')!=-1:
                        try:
                            e = embed(title = ':loudspeaker:공지',description=m)
                            e.set_footer(text = '문의 : GODMOONL#7059')
                            print(channel.name)
                            await app.send_message(channel,embed=e)
                        except:
                            continue
        await app.send_message(message.channel,'공지 발송 완료')                 
    if message.content == '!정보':
        e = info()
        await app.send_message(message.channel,embed=e)

    if message.content == '!서버리스트':
        e = embed(title = '갓봇 서버리스트!',description = '갓봇이 있는 서버를 불러옵니다', color=0x00C853)
        for i,s in enumerate(app.servers):
            e.add_field(name=i+1,value=s.name)
        await app.send_message(message.channel,embed=e)       
    for i in range(0,2):
        if message.content == a[i]:
            await app.send_message(message.channel,random.choice(b[i]))

    if message.content.startswith('!따라해 '):
        ans = message.content.split('!따라해')[1]
        await app.send_message(message.channel,ans)
    
    if message.content.startswith('!골라 '): 
        tmp = message.content.split('!골라 ')[1]
        ans = random.choice(tmp.split('/'))
        e = embed(title="갓봇의 선택은?",description=ans,color=0x00C853)
        await app.send_message(message.channel,embed=e)

    if message.content.startswith('!확률 '):
        ans = str(random.randrange(0,100))
        q = message.content.split('!확률 ')[1]
        e = embed(title=q+"은?",description=ans+"%입니다",color=0x00C853)
        await app.send_message(message.channel,embed=e)

    if message.content == '!프사':
        e = embed(title="당신의 프로필 사진",color=0x00C853)
        e.set_image(url=message.author.avatar_url)
        await app.send_message(message.channel,embed=e)    

    if message.content.startswith('!프사 '):
        e = embed(title="맨션한 사용자의 프로필 사진",color=0x00C853)
        if not message.mentions:
            e = embed(title="에러!",description="에러 발생")
            await app.send_message(message.channel,embed=e)
        else:
            user = message.mentions[0]
            e.set_image(url=user.avatar_url)
            await app.send_message(message.channel,embed=e)
            
    if message.content == '!돈순위':	
        e = game.rank()
        await app.send_message(message.channel,embed=e)	

    if message.content == '!돈줘':	
        uid = message.author.id	
        e = game.money(uid)
        await app.send_message(message.channel,embed=e)

    if message.content.startswith('!위키 '):
        msg = await app.send_message(message.channel,'로드 중입니다..')
        m = message.content[4:]
        ans = soup.wiki(m)
        await app.delete_message(msg)
        if not ans:
            e = embed(title = '오류',description = '위키피디아에 없는 문서입니다',color=0xF44336)
            await app.send_message(message.channel,embed=e)
        else:
            e = embed(title = m+" 검색결과")
            e.add_field(name = '내용',value = ans)
            e.set_footer(text='ko.wikipedia.org 위키피디아')
            await app.send_message(message.channel,embed=e)

    if message.content.startswith('!나무위키 '):
        msg = await app.send_message(message.channel,'로드 중입니다..')
        m = message.content[6:]
        ans = soup.namu(m)
        await app.delete_message(msg)
        if not ans:
            e = embed(title = '오류',description = '나무위키에 없는 문서입니다',color=0xF44336)
            await app.send_message(message.channel,embed=e)
        else:
            e = embed(title = m+" 검색결과",color=0x00A495)
            e.add_field(name = '내용',value = ans)
            e.set_footer(text='namu.wiki 나무위키')
            await app.send_message(message.channel,embed=e)

    if message.content.startswith('!날씨 '):
        msg = await app.send_message(message.channel,'로드 중입니다..')
        m = message.content[4:]
        ans = soup.Weather(m)
        await app.delete_message(msg)
        if ans.temp == 999:
            e = embed(title = '오류',description = '없는 지역입니다',color=0xF44336)
            await app.send_message(message.channel,embed=e)
        else:
            e = embed(title = m+" 날씨 : "+ans.cast,color=ans.color)
            e.add_field(name = '온도',value = ans.temp)
            e.add_field(name = '미세먼지',value = ans.aq[2])
            e.add_field(name = '초미세먼지',value = ans.aq[4])
            e.add_field(name = '오존농도',value = ans.aq[6])
            e.set_footer(text='naver.com 네이버')
            await app.send_message(message.channel,embed=e)

    if message.content.startswith('!영어위키 '):
        m = message.content[6:]
        ans = soup.enwiki(m)
        if not ans:
            e = embed(title = '오류',description = '영어 위키피디아에 없는 문서입니다')
            await app.send_message(message.channel,embed=e)
        else:
            e = embed(title = m+" 검색결과")
            e.add_field(name = '내용',value = ans)
            e.set_footer(text='en.wikipedia.org 위키피디아')
            await app.send_message(message.channel,embed=e)

    if message.content == '!멜론':
        msg = await app.send_message(message.channel,'로드 중입니다..')
        e = embed(title='멜론차트 TOP 10',description = '멜론차트 상위 10위를 불러옵니다',color = 0x04D939)
        ans = soup.Melon()
        for i in range(10):
            e.add_field(name = i+1,value = ans.tag[i].text)
        await app.delete_message(msg)
        await app.send_message(message.channel,embed=e)
        
app.run(token)