import sqlite3

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

def wordCountF(word):
    c,db = connect()
    ret = c.execute("SELECT count FROM fake_words WHERE word = ?", (word,)).fetchone()
    close(db)
    return ret

def wordCountT(word):
    c,db = connect()
    ret = c.execute("SELECT count FROM true_words WHERE word = ?", (word,)).fetchone()
    close(db)
    return ret

def getRandomFakeWord():
    c,db = connect()
    ret = c.execute("SELECT * FROM fake_words ORDER BY NEWID()").fetchone()
    close(db)
    return [ret[0], ret[1], ret[2]]

def getRandomTrueWord():
    c,db = connect()
    ret = c.execute("SELECT * FROM true_wprds ORDER BY NEWID()").fetchone()
    close(db)
    return [ret[0], ret[1], ret[2]]
