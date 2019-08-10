import time
import sqlite3
import discord

embed = discord.Embed

conn = sqlite3.connect('db')
cur = conn.cursor()

def rank():
    cur.execute('SELECT * FROM users ORDER BY money DESC')	
    l = cur.fetchall()	
    e = embed(title = "돈순위!",description="돈순위 상위 5명을 불러옵니다",color=0x00C853)	
    for i in range(0,5):	
        e.add_field(name =str(i+1)+'위',value='<@%s>\n%d원'%(l[i][1],l[i][0]))
    return e
    
def money(uid):
    cur.execute('SELECT * FROM users WHERE id=?',[uid])	
    l = cur.fetchone()	
    m = ""	
    if l is None:	
        m = "5000"	
        cur.execute('INSERT INTO users VALUES(?,?,?);',(m,uid,time.time()))	
        conn.commit()	
        cur.execute('SELECT * FROM users WHERE id=?',[uid])	
        l = cur.fetchone()	
    elif l[2]+300 <= time.time():	
        m = str(int(l[0])+5000)	
        cur.execute('UPDATE users SET money = ?, time=? WHERE id = ?',(m,time.time(),uid))	
        conn.commit()	
    if m=="":	
        e = embed(title="오류",description='돈은 5분에 한번씩 받을 수 있습니다 \n'+str(int((l[2]+300)-time.time()))+'초 남았습니다',color=0xF44336)	
    else:	
        e = embed(title = "돈을 받았습니다.",description = '당신의 돈은 '+m+'원입니다',color=0x00C853)	
    return e