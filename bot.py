import asyncio
import discord
import time
import random

app = discord.Client()
user = discord.User()

token = "토큰을 입력"
uptime = time.time()
@app.event
async def on_ready():
    print("다음으로 로그인 완료 :")
    print(app.user.name)
    print(app.user.id)
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    await app.change_presence(game=discord.Game(name="!야 라고 해보세요!"))
@app.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == '!정보':
        end = time.time()-uptime
        ut = int(end)
        min = int(ut/60)
        hour = int(min/60)
        day = str(int(hour/24))
        hour = str(hour%24)
        ut=str(ut%60)
        min=str(min%60)
        embed = discord.Embed(title="갓봇 정보!", description="개발자 : GODMOONL#7059\n업타임 : "+day+"일 "+hour+"시 "+min+"분 "+ut+"초 ", color=0x00ff00)
        await app.send_message(message.channel,embed=embed)
    if message.content == '!야':
        rnum = random.randrange(0,6)
        ans = ['🤷‍왜','답변','외수영장','놀자','나두','🤷‍왜']
        await app.send_message(message.channel,ans[rnum])

    if message.content == '!이런':
        rnum = random.randrange(0,3)
        ans = ['🤦‍저런','ㅇㅅㅇ','🤦‍저런']
        await app.send_message(message.channel,ans[rnum])

    if message.content == '!저런':
        rnum = random.randrange(0,3)
        ans = ['🤦‍이런','ㅇㅅㅇ','🤦‍이런']
        await app.send_message(message.channel,ans[rnum])

    if message.content.startswith('!따라해 '):
        ans = message.content.split('!따라해')[1]
        await app.send_message(message.channel,ans)
    
    if message.content.startswith('!골라 '):
        rnum = random.randrange(0,1)
        tmp = message.content.split('!골라 ')[1]
        ans = tmp.split('/')[rnum]
        embed = discord.Embed(title="갓봇의 선택은?",description=ans)
        await app.send_message(message.channel,embed=embed)

    if message.content.startswith('!확률 '):
        ans = str(random.randrange(0,100))
        q = message.content.split('!확률 ')[1]
        embed = discord.Embed(title=q+"은?",description=ans+"%입니다")
        await app.send_message(message.channel,embed=embed)

    if message.content == '!프사':
        embed = discord.Embed(title="사용자의 프로필 사진")
        user = message.author
        embed.set_image(url=user.avatar_url)
        await app.send_message(message.channel,embed=embed)

    if message.content.startswith('!프사 '):
        embed = discord.Embed(title="맨션한 사용자의 프로필 사진")
        if not message.mentions:
            embed = discord.Embed(title="에러!",description="에러 발생")
            await app.send_message(message.channel,embed=embed)
        else:
            user = message.mentions[0]
            embed.set_image(url=user.avatar_url)
            await app.send_message(message.channel,embed=embed)
    
        
    

app.run(token)