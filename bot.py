import asyncio
import discord
import time
import random
import sqlite3
import setting

conn = sqlite3.connect('db')
cur = conn.cursor()

app = discord.Client()
embed=discord.Embed

token = setting.token

uptime = time.time()

a = setting.a
b = setting.b

@app.event
async def on_ready():
    print("다음으로 로그인 완료 :")
    print(app.user.name)
    print(app.user.id)
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    await app.change_presence(game=discord.Game(name="!도움 이라고 해보세요!"))

@app.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == '!도움':
        r = open('update.txt',mode='rt',encoding = 'utf-8')
        rows = r.readlines()
        e = embed(title = '갓봇 도움!')
        for i in rows:
            e.add_field(name = i.split('/')[0],value=i.split('/')[1])
        await app.send_message(message.channel,embed=e)

    if message.content == '!정보':
        end = time.time()-uptime
        ut = int(end)
        min = int(ut/60)
        hour = int(min/60)
        day = str(int(hour/24))
        hour = str(hour%24)
        ut=str(ut%60)
        min=str(min%60)
        e = embed(title="갓봇 정보!", description="개발자 : GODMOONL#7059\n업타임 : "+day+"일 "+hour+"시간 "+min+"분 "+ut+"초 ", color=0x00ff00)
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
        e = embed(title="갓봇의 선택은?",description=ans)
        await app.send_message(message.channel,embed=e)

    if message.content.startswith('!확률 '):
        ans = str(random.randrange(0,100))
        q = message.content.split('!확률 ')[1]
        e = embed(title=q+"은?",description=ans+"%입니다")
        await app.send_message(message.channel,embed=e)

    if message.content == '!프사':
        e = embed(title="당신의 프로필 사진")
        e.set_image(url=message.author.avatar_url)
        await app.send_message(message.channel,embed=e)    

    if message.content.startswith('!프사 '):
        e = embed(title="맨션한 사용자의 프로필 사진")
        if not message.mentions:
            e = embed(title="에러!",description="에러 발생")
            await app.send_message(message.channel,embed=e)
        else:
            user = message.mentions[0]
            e.set_image(url=user.avatar_url)
            await app.send_message(message.channel,embed=e)
    
app.run(token)