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
             if wordCountF(i) == None:
                 addWordF(i)
                 print("added word: " + i + " to FALSE")
             else:
                 updateCountF(i)
                 print("updated: " + i + " in FALSE")

# populate true
with open('data/True (1).csv', 'r', encoding="utf8") as file:
     text=csv.reader(file)
     for row in text:
         row = row[1].strip().lower().replace(",", " ").replace(".", " ").replace("!", " ").replace("?", " ").replace(";", " ").replace("'", " ").replace('"', " ").replace('(', " ").replace(')', " ").replace('[', " ").replace(']', " ").replace('{', " ").replace('}', " ").replace(',', " ").replace('.', " ").replace('-', " ").replace('_', " ")
         words = row.split()
         for i in words:
             if wordCountT(i) == None:
                 addWordT(i)
                 print("added word: " + i + " to TRUE")
             else:
                 updateCountT(i)
                 print("updated: " + i + " in TRUE")
