import csv
import random
from db import *

build()

# populate fake
with open('data/Fake (1).csv', 'r', encoding="utf8") as file:
     text=csv.reader(file)
     for row in text:
         row = row[1].strip().lower().replace(",", " ").replace(".", " ").replace("!", " ").replace("?", " ").replace(";", " ").replace("'", " ").replace('"', " ").replace('(', " ").replace(')', " ").replace('[', " ").replace(']', " ").replace('{', " ").replace('}', " ").replace(',', " ").replace('.', " ").replace('-', " ").replace('_', " ")
         words = row.split()
         for i in words:
             print(wordInfoF(i))
             if len(wordInfoF(i)) == 0:
                 addWordF(i)
                 print("added word: " + i)
             else:
                 updateCountF(i)

# populate true
with open('data/True (1).csv', 'r', encoding="utf8") as file:
     text=csv.reader(file)
     for row in text:
         row = row[1].strip().lower().replace(",", " ").replace(".", " ").replace("!", " ").replace("?", " ").replace(";", " ").replace("'", " ").replace('"', " ").replace('(', " ").replace(')', " ").replace('[', " ").replace(']', " ").replace('{', " ").replace('}', " ").replace(',', " ").replace('.', " ").replace('-', " ").replace('_', " ")
         words = row.split()
         for i in words:
             if len(wordInfoT(i)) == 0:
                 addWordT(i)
                 print("added word: " + i)
             else:
                 updateCountT(i)
