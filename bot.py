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

a = ['!야','!이런','!저런']
b = [['🤷‍왜','답변','외수영장','놀자','나두','🤷‍왜'],['🤦‍저런','ㅇㅅㅇ','🤦‍저런'],['🤦‍이런','ㅇㅅㅇ','🤦‍이런']]

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
<<<<<<< HEAD

   
=======
        
>>>>>>> eeeb553f146d30455f7c0d5ae43a8ed8fa3876fa
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
            
    if message.content == '!돈순위':
        cur.execute('SELECT * FROM users ORDER BY money DESC')
        l = cur.fetchall()
        e = embed(title = "돈순위!",description="돈순위 상위 5명을 불러옵니다")
        for i in range(0,5):
            e.add_field(name =str(i+1)+'위',value='<@%s>\n%d원'%(l[i][1],l[i][0]))
        await app.send_message(message.channel,embed=e)
        
    if message.content == '!돈줘':
        uid = message.author.id
        cur.execute('SELECT * FROM users WHERE id=?',[uid])
        l = cur.fetchone()
        m = ""
        if l is None:
            m = "5000"
            print(uid)
            cur.execute('INSERT INTO users VALUES(?,?,?);',(m,uid,time.time()))
            conn.commit()
            cur.execute('SELECT * FROM users WHERE id=?',[uid])
            l = cur.fetchone()
        elif l[2]+300 <= time.time():
            m = str(int(l[0])+5000)
            cur.execute('UPDATE users SET money = ?, time=? WHERE id = ?',(m,time.time(),uid))
            conn.commit()
        if m=="":
            e = embed(title="오류",description='돈은 5분에 한번씩 받을 수 있습니다 \n'+str(int((l[2]+300)-time.time()))+'초 남았습니다')
        else:
            e = embed(title = "돈을 받았습니다.",description = '당신의 돈은 '+m+'원입니다')
        await app.send_message(message.channel,embed=e)

app.run(token)