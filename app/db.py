import sqlite3

def build():
    database = sqlite3.connect("SALT.db")
    c = database.cursor()
    
    c.execute("CREATE TABLE IF NOT EXISTS user(username TEXT, password TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS articles(title TEXT, content TEXT, topic TEXT, real BOOLEAN)")
    c.execute("CREATE TABLE IF NOT EXISTS loaded_articles(link TEXT, rating_percentage INTEGER)")
    
    database.commit()
    database.close()
    