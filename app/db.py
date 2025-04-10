import sqlite3


USER_FILE = "SALT.db"
def build():
    createUsers()
    createArticleInfo()
    createWordCountInfo()
    createFontSizeInfoF()
    createFontSizeInfoR()
    #c.execute("CREATE TABLE IF NOT EXISTS loaded_articles(link TEXT, rating_percentage INTEGER)")
    
    
    
def createUsers():
    users = sqlite3.connect(USER_FILE)
    c = users.cursor()
    command = "CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)"
    c.execute(command)
    users.commit()
    
def createArticleInfo():
    articles = sqlite3.connect(USER_FILE)
    c = articles.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS articles(title TEXT, content TEXT)")
    c.execute(command)
    articles.commit()
    
def createWordCountInfoF():
    wordCountF = sqlite3.connect(USER_FILE)
    c = wordCountF.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS wordCountF(word TEXT, count INT)")
    wordCountF.commit()
    
def createWordCountInfoR():
    wordCountR = sqlite3.connect(USER_FILE)
    c = wordCountR.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS wordCountR(word TEXT, count INT)")
    wordCountR.commit()
    
def addWordCountInfoF(word, count):
    wordCountF = sqlite3.connect(USER_FILE)
    c = wordCountF.cursor()
    c.execute("INSERT INTO wordCountF(word, count) VALUES (?, ?)", (word, count))
    wordCountF.commit()
    
def addWordCountInfoR(word, count):
    wordCountR = sqlite3.connect(USER_FILE)
    c = wordCountR.cursor()
    c.execute("INSERT INTO wordCountR(word, count) VALUES (?, ?)", (word, count))
    wordCountR.commit()
    

def updateCountF(word):
    wordCountF = sqlite3.connect(USER_FILE)
    c = wordCountF.cursor()
    c.execute("SELECT count FROM wordCountF WHERE word = ?", (word,))
    data = c.fetchone()
    countF = int(data[0])+1
    c.execute("UPDATE wordCountF SET count = ? WHERE word = ?", (countF, word))
    wordCountF.commit()

def updateCountR(word):
    wordCountR = sqlite3.connect(USER_FILE)
    c = wordCountR.cursor()
    c.execute("SELECT count FROM wordCountR WHERE word = ?", (word,))
    data = c.fetchone()
    countR = int(data[0])+1
    c.execute("UPDATE wordCountR SET count = ? WHERE word = ?", (countR, word))
    wordCountR.commit()
    
def returnWordCountF():
    wordCountF = sqlite3.connect(USER_FILE)
    c = wordCountF.cursor()
    c.execute("SELECT * FROM wordCountF")
    return c.fetchall()

def returnWordCountR():
    wordCountF = sqlite3.connect(USER_FILE)
    c = wordCountF.cursor()
    c.execute("SELECT * FROM wordCountF")
    return c.fetchall()
    
def updateArticleInfo(username, title, content):
    users = sqlite3.connect(USER_FILE)
    c = users.cursor()
    if (c.execute("SELECT 1 FROM articles WHERE username=?", (username,))).fetchone() == None:
        return
    c.execute("UPDATE webinfo SET title=?, content=? WHERE username=?", (title, content, username))
    users.commit()
    
 
def createFontSizeInfoF():
    fontsF = sqlite3.connect(USER_FILE)
    c = fontsF.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS fontsF(word TEXT, size REAL)")
    fontsF.commit()
    
def createFontSizeInfoR():
    fontsR = sqlite3.connect(USER_FILE)
    c = fontsR.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS fontsR(word TEXT, size REAL)")
    fontsR.commit()
    
def addFontSizeInfoF(word, size):
    fontsF = sqlite3.connect(USER_FILE)
    c = fontsF.cursor()
    c.execute("INSERT INTO fontsF(word, size) VALUES (?, ?)", (word, size))
    fontsF.commit()

def addFontSizeInfoR(word, size):
    fontsR = sqlite3.connect(USER_FILE)
    c = fontsR.cursor()
    c.execute("INSERT INTO fontsR(word, size) VALUES (?, ?)", (word, size))
    fontsR.commit()

def returnFontTableF():
    fontsF = sqlite3.connect(USER_FILE)
    c = fontsF.cursor()
    c.execute("SELECT * FROM fontsF")
    return c.fetchall()

def returnFontTableR():
    fontsR = sqlite3.connect(USER_FILE)
    c = fontsR.cursor()
    c.execute("SELECT * FROM fontsR")
    return c.fetchall()

def deleteFontTableF():
    fontsF = sqlite3.connect(USER_FILE)
    c = fontsF.cursor()
    c.execute("DELETE FROM fontsF")
    fontsF.commit()
    
def deleteFontTableR():
    fontsR = sqlite3.connect(USER_FILE)
    c = fontsR.cursor()
    c.execute("DELETE FROM fontsR")
    fontsR.commit()