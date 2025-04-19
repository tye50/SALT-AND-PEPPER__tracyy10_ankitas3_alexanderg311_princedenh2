import csv
import random
from db import *

build()

# populate fake
# with open('data/sectionF.csv', 'r', encoding="utf8") as file:
#      text=csv.reader(file)
#      for row in text:
#          row = row[1].strip().lower().replace("/", " ").replace(":", " ").replace(",", " ").replace(".", " ").replace("!", " ").replace("?", " ").replace(";", " ").replace("'", "").replace('"', " ").replace('(', " ").replace(')', " ").replace('[', " ").replace(']', " ").replace('{', " ").replace('}', " ").replace(',', " ").replace('.', " ").replace('-', "").replace('_', " ")
#          words = row.split()
#          for i in words:
#              if wordCountF(i) == 0:
#                  addWordF(i)
#                  #print("added word: " + i + " to FALSE")
#              else:
#                  updateCountF(i)
#                  #print("updated: " + i + " in FALSE")
# print("Finished loading this section of Fake data set.")

# populate true
with open('data/sectionT.csv', 'r', encoding="utf8") as file:
     text=csv.reader(file)
     for row in text:
         row = row[1].strip().lower().replace("/", " ").replace(":", " ").replace(",", " ").replace(".", " ").replace("!", " ").replace("?", " ").replace(";", " ").replace("'", "").replace('"', " ").replace('(', " ").replace(')', " ").replace('[', " ").replace(']', " ").replace('{', " ").replace('}', " ").replace(',', " ").replace('.', " ").replace('-', "").replace('_', " ")
         words = row.split()
         for i in words:
             if wordCountT(i) == 0:
                 addWordT(i)
                 #print("added word: " + i + " to TRUE")
             else:
                 updateCountT(i)
                 #print("updated: " + i + " in TRUE")
print("Finished loading this section of True data set.")
##################################  DO NOT RUN THIS FILE  #########################################