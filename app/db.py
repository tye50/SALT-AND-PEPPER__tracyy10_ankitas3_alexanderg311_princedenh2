import sqlite3
import json
import random
import copy

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

# build()

#########################################################################################

filler = {'call', "eye","the", "a", "that", "he", "her", "his", "him", "if", "they",'upon', 'still', 'nevertheless', 'down', 'every', 'forty', '‘re', 'always', 'whole', 'side', "n't", 'now', 'however', 'an', 'show', 'least', 'give', 'below', 'did', 'sometimes', 'which', "'s", 'nowhere', 'per', 'hereupon', 'yours', 'she', 'moreover', 'eight', 'somewhere', 'within', 'whereby', 'few', 'has', 'so', 'have', 'for', 'noone', 'top', 'were', 'those', 'thence', 'eleven', 'after', 'no', '’ll', 'others', 'ourselves', 'themselves', 'though', 'that', 'nor', 'just', '’s', 'before', 'had', 'toward', 'another', 'should', 'herself', 'and', 'these', 'such', 'elsewhere', 'further', 'next', 'indeed', 'bottom', 'anyone', 'his', 'each', 'then', 'both', 'became', 'third', 'whom', '‘ve', 'mine', 'take', 'many', 'anywhere', 'to', 'well', 'thereafter', 'besides', 'almost', 'front', 'fifteen', 'towards', 'none', 'be', 'herein', 'two', 'using', 'whatever', 'please', 'perhaps', 'full', 'ca', 'we', 'latterly', 'here', 'therefore', 'us', 'how', 'was', 'made', 'the', 'or', 'may', '’re', 'namely', "'ve", 'anyway', 'amongst', 'used', 'ever', 'of', 'there', 'than', 'why', 'really', 'whither', 'in', 'only', 'wherein', 'last', 'under', 'own', 'therein', 'go', 'seems', '‘m', 'wherever', 'either', 'someone', 'up', 'doing', 'on', 'rather', 'ours', 'again', 'same', 'over', '‘s', 'latter', 'during', 'done', "'re", 'put', "'m", 'much', 'neither', 'among', 'seemed', 'into', 'once', 'my', 'otherwise', 'part', 'everywhere', 'never', 'myself', 'must', 'will', 'am', 'can', 'else', 'although', 'as', 'beyond', 'are', 'too', 'becomes', 'does', 'a', 'everyone', 'but', 'some', 'regarding', '‘ll', 'against', 'throughout', 'yourselves', 'him', "'d", 'it', 'himself', 'whether', 'move', '’m', 'hereafter', 're', 'while', 'whoever', 'your', 'first', 'amount', 'twelve', 'serious', 'other', 'any', 'off', 'seeming', 'four', 'itself', 'nothing', 'beforehand', 'out', 'very', 'already', 'various', 'until', 'hers', 'they', 'not', 'them', 'where', 'would', 'since', 'everything', 'at', 'together', 'yet', 'more', 'six', 'back', 'with', 'thereupon', 'becoming', 'around', 'due', 'keep', 'somehow', 'n‘t', 'across', 'all', 'when', 'i', 'empty', 'nine', 'five', 'get', 'see', 'been', 'name', 'between', 'hence', 'ten', 'several', 'from', 'whereupon', 'through', 'hereby', "'ll", 'alone', 'something', 'formerly', 'without', 'above', 'onto', 'except', 'enough', 'become', 'behind', '’d', 'its', 'most', 'n’t', 'might', 'whereas', 'anything', 'if', 'her', 'via', 'fifty', 'is', 'thereby', 'twenty', 'often', 'whereafter', 'also', 'anyhow', 'cannot', 'our', 'could', 'because', 'who', 'beside', 'by', 'whence', 'being', 'meanwhile', 'this', 'afterwards', 'whenever', 'mostly', 'what', 'one', 'nobody', 'seem', 'less', 'do', '‘d', 'say', 'thus', 'unless', 'along', 'yourself', 'former', 'thru', 'he', 'hundred', 'three', 'sixty', 'me', 'sometime', 'whose', 'you', 'quite', '’ve', 'about', 'even'}
t = returnT()
f = returnF()

all_dictF=[]
all_dictT=[]

for i in range(0,len(t)):
    if t[i][0] not in filler:
        single_dict = dict(name=t[i][0], count=(t[i][1]), color=t[i][2])
        all_dictT.append(single_dict)

for i in range(0,len(f)):
    if f[i][0] not in filler:
        single_dict = dict(name=f[i][0], count=(f[i][1]), color=f[i][2])
        all_dictF.append(single_dict)

def change_size(modify_dict):
    total_dict = all_dictF + all_dictT
    hi=total_dict[0].get("count")
    lo=total_dict[0].get("count")
    for i in total_dict:
        if i.get("count")>hi:
            hi=i.get("count")
        elif i.get("count")<lo:
            lo=i.get("count")
    diff = hi-lo
    rate = diff/1000
    for i in modify_dict:
        font_size=(i.get("count")/hi)*100
        if font_size <= .01:
            i["count"] = 10
        elif font_size> .01 and font_size<= .02:
            i["count"] = 15
        elif font_size> .02 and font_size<= .05:
            i["count"] = 20
        elif font_size> .05 and font_size<= .1:
            i["count"] = 30
        elif font_size> .1 and font_size<= .3:
            i["count"] = 45
        elif font_size> .4 and font_size<= .5:
            i["count"] = 60
        elif font_size> .5 and font_size<= 2:
            i["count"] = 65
        elif font_size> 2 and font_size<= 5:
            i["count"] = 70
        elif font_size> 5 and font_size<= 10:
            i["count"] = 75
        elif font_size> lo+(4*rate) and font_size<= lo + (5*rate):
            i["count"] = 80
        elif font_size> lo+(5*rate) and font_size<= lo + (6*rate):
            i["count"] = 85
        elif font_size> lo+(6*rate) and font_size<= lo + (7*rate):
            i["count"] = 90
        elif font_size> lo+(7*rate) and font_size<= lo + (8*rate):
            i["count"] = 95
        elif font_size> lo+(8*rate) and font_size<= lo + (9*rate):
            i["count"] = 100
        elif font_size> lo+(9*rate) and font_size<= lo + (10*rate):
            i["count"] = 110
        elif font_size> lo+(10*rate) and font_size<= lo + (11*rate):
            i["count"] = 120
        else:
            i["count"] = 150
    return modify_dict

all_dictF = change_size(copy.deepcopy(all_dictF))
all_dictT = change_size(copy.deepcopy(all_dictT))

all_dictT.extend(all_dictF)
with open("pleasework.json", "w") as f:
    json.dump(all_dictT, f)
