import sqlite3
import json

USER_FILE = "TESTING.db"
def build():
    createWordCountInfo()

def createWordCountInfo():
    wordCount = sqlite3.connect(USER_FILE)
    c = wordCount.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS wordCount(word TEXT, count INT, color TEXT)")
    wordCount.commit()
    
def addWordCountInfo(word, count, color):
    wordCount = sqlite3.connect(USER_FILE)
    c = wordCount.cursor()
    c.execute("INSERT INTO wordCount(word, count, color) VALUES (?, ?, ?)", (word, count, color))
    wordCount.commit()

def returnWordCountInfo():
    wordCount = sqlite3.connect(USER_FILE)
    c = wordCount.cursor()
    c.execute("SELECT * FROM wordCount")
    wordCount.commit()
    return c.fetchall()
 
build()
addWordCountInfo("hi", 50, "blue")
addWordCountInfo("By", 20, "red")
r = returnWordCountInfo()

all_dict=[]
for i in range(0,len(r)):
    single_dict = dict(name=r[i][0], count=r[i][1], color=r[i][2])
    all_dict.append(single_dict)
    

with open("pleasework.json", "w") as f:
    json.dump(all_dict, f)
    

print("hi")




    