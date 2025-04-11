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
    c.execute("CREATE TABLE IF NOT EXISTS fake_words(word TEXT, count INTEGER)")
    c.execute("CREATE TABLE IF NOT EXISTS true_words(word TEXT, count INTEGER)")
    c.execute("CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)")
    close(db)

def addWordF(word):
    c,db = connect()
    c.execute("INSERT INTO fake_words(word, count) VALUES (?, ?)", (word, 1))
    close(db)

def updateCountF(word):
    c,db = connect()
    data = c.execute("SELECT count FROM fake_words WHERE word = ?", (word,)).fetchone()
    countF = int(data[0])+1
    c.execute("UPDATE fake_words SET count = ? WHERE word = ?", (countF, word))
    close(db)
    
def addWordT(word):
    c,db = connect()
    c.execute("INSERT INTO true_words(word, count) VALUES (?, ?)", (word, 1))
    close(db)

def updateCountT(word):
    c,db = connect()
    data = c.execute("SELECT count FROM true_words WHERE word = ?", (word,)).fetchone()
    countT = int(data[0])+1
    c.execute("UPDATE true_words SET count = ? WHERE word = ?", (countT, word))
    close(db)

def wordInfoF(word):
    c,db = connect()
    ret = ("SELECT * FROM fake_words WHERE word = ?", (word,)).fetchall()
    close(db)
    return ret

def wordInfoT(word):
    c,db = connect()
    ret = ("SELECT * FROM true_words WHERE word = ?", (word,)).fetchall()
    close(db)
    return ret