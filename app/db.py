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
    print("Database successfully created.")

def updateCountF(word):
    c, db = connect()
    c.execute("SELECT count FROM wordCountF WHERE word = ?", (word,))
    
    
    wordCountF = sqlite3.connect(USER_FILE)
    c = wordCountF.cursor()
    c.execute("SELECT count FROM wordCountF WHERE word = ?", (word,))
    data = c.fetchone()
    countF = int(data[0])+1
    c.execute("UPDATE wordCountF SET count = ? WHERE word = ?", (countF, word))
    wordCountF.commit()