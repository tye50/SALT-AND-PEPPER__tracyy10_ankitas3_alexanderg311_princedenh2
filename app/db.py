import sqlite3

def build():
    database = sqlite3.connect("SALT.db")
    c = database.cursor()
    createUsers()
    createArticleInfo()
    createFontSizeInfo()
    c.execute("CREATE TABLE IF NOT EXISTS loaded_articles(link TEXT, rating_percentage INTEGER)")
    
    database.commit()
    database.close()
    
    
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
    
    
def updateArticleInfo(username, title, content):
    users = sqlite3.connect(USER_FILE)
    c = users.cursor()
    if (c.execute("SELECT 1 FROM articles WHERE username=?", (username,))).fetchone() == None:
        return
    c.execute("UPDATE webinfo SET title=?, content=? WHERE username=?", (title, content, username))
    users.commit()
    
def createFontSizeInfo():
    fonts = sqlite3.connect(USER_FILE)
    c = fonts.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS articles(word TEXT, fontSize REAL")
    c.execute(command)
    fonts.commit()
    
def updateArticleInfo(username, title, content):
    users = sqlite3.connect(USER_FILE)
    c = users.cursor()
    if (c.execute("SELECT 1 FROM articles WHERE username=?", (username,))).fetchone() == None:
        return
    c.execute("UPDATE webinfo SET title=?, content=? WHERE username=?", (title, content, username))
    users.commit()

