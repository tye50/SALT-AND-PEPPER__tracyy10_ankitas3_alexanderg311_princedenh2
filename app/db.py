import sqlite3
import json
import random

def connect():
    db = sqlite3.connect("SALT.db")
    c = db.cursor()
    return c, db

def close(db):
    db.commit()
    db.close()

def build():
    c,db = connect()
    c.execute("CREATE TABLE IF NOT EXISTS fake_words(word TEXT, count INTEGER, color TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS true_words(word TEXT, count INTEGER, color TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)")
    close(db)

def addWordF(word):
    c,db = connect()
    c.execute("INSERT INTO fake_words(word, count, color) VALUES (?, ?, ?)", (word, 1, 'red'))
    close(db)

def updateCountF(word):
    c,db = connect()
    data = c.execute("SELECT count FROM fake_words WHERE word = ?", (word,)).fetchone()
    countF = int(data[0])+1
    c.execute("UPDATE fake_words SET count = ? WHERE word = ?", (countF, word))
    close(db)
    
def addWordT(word):
    c,db = connect()
    c.execute("INSERT INTO true_words(word, count, color) VALUES (?, ?, ?)", (word, 1, 'blue'))
    close(db)

def updateCountT(word):
    c,db = connect()
    data = c.execute("SELECT count FROM true_words WHERE word = ?", (word,)).fetchone()
    countT = int(data[0])+1
    c.execute("UPDATE true_words SET count = ? WHERE word = ?", (countT, word))
    close(db)

def returnWordsF():
    c,db = connect()
    c.execute("SELECT word FROM fake_words")
    db.commit()
    fin = []
    for i in c.fetchall():
        for j in i:
            fin.append(j)
    return fin

def returnWordsT():
    c,db = connect()
    c.execute("SELECT word FROM true_words")
    db.commit()
    fin = []
    for i in c.fetchall():
        for j in i:
            fin.append(j)
    return fin

def wordCountF(word):
    c,db = connect()
    ret = c.execute("SELECT count FROM fake_words WHERE word = ?", (word,))
    db.commit()
    if word not in returnWordsF():
        return 0
    else:
        return list(c.fetchone())[0]

def wordCountT(word):
    c,db = connect()
    ret = c.execute("SELECT count FROM true_words WHERE word = ?", (word,))
    db.commit()
    if word not in returnWordsT():
        return 0
    else:
        return list(c.fetchone())[0]

def getRandomFakeWord():
    c,db = connect()
    ret = c.execute("SELECT * FROM fake_words ORDER BY RANDOM()").fetchone()
    close(db)
    return [ret[0], ret[1], ret[2]]

def getRandomTrueWord():
    c,db = connect()
    ret = c.execute("SELECT * FROM true_words ORDER BY RANDOM()").fetchone()
    close(db)
    return [ret[0], ret[1], ret[2]]

def attemptAddUser(username, password):
    c, db = connect()
    matching = c.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchall()
    if len(matching) == 0:
        c.execute("INSERT INTO users(username, password) VALUES (?, ?)", (username, password))
        close(db)
        return 0 # if 0 --> added
    close(db)
    return 1 # if 1 --> user exists

def getUser(user):
    c, db = connect()
    ret = c.execute("SELECT * FROM users WHERE username = ?", (user,)).fetchone()
    if ret == None:
        close(db)
        return 0 # if 0 --> doesn't exit
    close(db)
    return [ret[0], ret[1]]

def returnF():
    c,db = connect()
    ret = c.execute("SELECT * FROM fake_words").fetchall()
    db.commit()
    return ret

def returnT():
    c,db = connect()
    ret = c.execute("SELECT * FROM true_words").fetchall()
    db.commit()
    return ret

def getRandomFakeWord():
    c,db = connect()
    ret = c.execute("SELECT * FROM fake_words ORDER BY RANDOM()").fetchone()
    close(db)
    return [ret[0], ret[1], ret[2]]



#########################################################################################
    
t = returnT()
f = returnF()

all_dictF=[]
all_dictT=[]

for i in range(0,len(t)):
    single_dict = dict(name=t[i][0], count=(t[i][1]), color=t[i][2])
    all_dictT.append(single_dict)

for i in range(0,len(f)):
    single_dict = dict(name=f[i][0], count=(f[i][1]), color=f[i][2])
    all_dictF.append(single_dict)
    
all_dictT.extend(all_dictF)

with open("pleasework.json", "w") as f:
    json.dump(all_dictT, f)
















