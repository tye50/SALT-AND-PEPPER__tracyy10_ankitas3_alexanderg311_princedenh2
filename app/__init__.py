from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from flask import flash
import os
import numpy as np 
import pandas as pd
import random



import sqlite3
import db
from db import *

import news_analysis

app = Flask(__name__)
secret = os.urandom(32)
app.secret_key = secret



fake = pd.read_csv(os.path.abspath('data/Fake (1).csv'))
real = pd.read_csv(os.path.abspath('data/True (1).csv'))


#add word and word count to table
#get word and word count from table to font size table

# default = spacy.load("en_core_web_lg")
# filler = en.Defaults.stop_words
filler = {"i ","me","my","myself","we","our","ours","ourselves","you","your","yours","yourself","yourselves","he","him","his","himself","she","her","hers","herself","it","its","itself","they","them","their","theirs","themselves","what","which","who","whom","this","that","these","those","am","is","are","was","were","be","been","being","have","has","had","having","do","does","did","doing","a","an","the","and","but","if","or","because","as","until","while","of","at","by","for","with","about","against","between","into","through","during","before","after","above","below","to","from","up","down","in","out","on","off","over","under","again","further","then","once","here","there","when","where","why","how","all","any","both","each","few","more","most","other","some","such","no","nor","not","only","own","same","so","than","too","very","s","t","can","will","just","don","should","now",'call', "eye","the", "a", "that", "he", "her", "his", "him", "if", "they",'upon', 'still', 'nevertheless', 'down', 'every', 'forty', '‘re', 'always', 'whole', 'side', "n't", 'now', 'however', 'an', 'show', 'least', 'give', 'below', 'did', 'sometimes', 'which', "'s", 'nowhere', 'per', 'hereupon', 'yours', 'she', 'moreover', 'eight', 'somewhere', 'within', 'whereby', 'few', 'has', 'so', 'have', 'for', 'noone', 'top', 'were', 'those', 'thence', 'eleven', 'after', 'no', '’ll', 'others', 'ourselves', 'themselves', 'though', 'that', 'nor', 'just', '’s', 'before', 'had', 'toward', 'another', 'should', 'herself', 'and', 'these', 'such', 'elsewhere', 'further', 'next', 'indeed', 'bottom', 'anyone', 'his', 'each', 'then', 'both', 'became', 'third', 'whom', '‘ve', 'mine', 'take', 'many', 'anywhere', 'to', 'well', 'thereafter', 'besides', 'almost', 'front', 'fifteen', 'towards', 'none', 'be', 'herein', 'two', 'using', 'whatever', 'please', 'perhaps', 'full', 'ca', 'we', 'latterly', 'here', 'therefore', 'us', 'how', 'was', 'made', 'the', 'or', 'may', '’re', 'namely', "'ve", 'anyway', 'amongst', 'used', 'ever', 'of', 'there', 'than', 'why', 'really', 'whither', 'in', 'only', 'wherein', 'last', 'under', 'own', 'therein', 'go', 'seems', '‘m', 'wherever', 'either', 'someone', 'up', 'doing', 'on', 'rather', 'ours', 'again', 'same', 'over', '‘s', 'latter', 'during', 'done', "'re", 'put', "'m", 'much', 'neither', 'among', 'seemed', 'into', 'once', 'my', 'otherwise', 'part', 'everywhere', 'never', 'myself', 'must', 'will', 'am', 'can', 'else', 'although', 'as', 'beyond', 'are', 'too', 'becomes', 'does', 'a', 'everyone', 'but', 'some', 'regarding', '‘ll', 'against', 'throughout', 'yourselves', 'him', "'d", 'it', 'himself', 'whether', 'move', '’m', 'hereafter', 're', 'while', 'whoever', 'your', 'first', 'amount', 'twelve', 'serious', 'other', 'any', 'off', 'seeming', 'four', 'itself', 'nothing', 'beforehand', 'out', 'very', 'already', 'various', 'until', 'hers', 'they', 'not', 'them', 'where', 'would', 'since', 'everything', 'at', 'together', 'yet', 'more', 'six', 'back', 'with', 'thereupon', 'becoming', 'around', 'due', 'keep', 'somehow', 'n‘t', 'across', 'all', 'when', 'i', 'empty', 'nine', 'five', 'get', 'see', 'been', 'name', 'between', 'hence', 'ten', 'several', 'from', 'whereupon', 'through', 'hereby', "'ll", 'alone', 'something', 'formerly', 'without', 'above', 'onto', 'except', 'enough', 'become', 'behind', '’d', 'its', 'most', 'n’t', 'might', 'whereas', 'anything', 'if', 'her', 'via', 'fifty', 'is', 'thereby', 'twenty', 'often', 'whereafter', 'also', 'anyhow', 'cannot', 'our', 'could', 'because', 'who', 'beside', 'by', 'whence', 'being', 'meanwhile', 'this', 'afterwards', 'whenever', 'mostly', 'what', 'one', 'nobody', 'seem', 'less', 'do', '‘d', 'say', 'thus', 'unless', 'along', 'yourself', 'former', 'thru', 'he', 'hundred', 'three', 'sixty', 'me', 'sometime', 'whose', 'you', 'quite', '’ve', 'about', 'even'}

fake['true'] = 0
real['true'] = 1
news = pd.concat([fake, real], ignore_index = True)
#news.drop(['subject', 'date'], axis=1)
#print(news.head(10))

fake_text = fake['text']
fake_title = fake['title']
real_text = real['text']
real_title = real['title']
fake_text_dict = {}
fake_title_dict = {}

real_text_dict = {}
real_title_dict = {}
    
    
@app.route("/")
def main():
    deleteFontTableF()
    deleteFontTableR()
    createFontSizeInfoF()
    createFontSizeInfoR()
    if 'username' in session:
        return redirect("/dashbord")
    fake = one()
    real = real_text_words()
    return render_template("main.html", fake=fake, real=real)

def words_counts():
    createWordCountInfoF()
    createWordCountInfoR()
    pli = []
    for i in range(0, len(fake_text)):
        title_words = fake_title[i].split(' ')
        n=[]
        rmov = "1234567890-`=@#!$%^&*(’),“—.:?/;[]_{}+”<>'\“\""
        for k in title_words:
            for j in k:
                if j in rmov:
                    k = k.replace(j," ")
            pli = k.split(' ')
            for b in pli:
                n.append(b)
        
        text_words = fake_text[i].split(' ')
        for k in text_words:
            for j in k:
                if j in rmov:
                    k = k.replace(j," ")
            pli = k.split(' ')
            for b in pli:
                n.append(b)
            
        for word in n:
            if word in fake_title_dict.keys():
                fake_title_dict[word] += 1
            else:
                fake_title_dict[word] = 1
        for word in m:
            if word in fake_text_dict.keys():
                fake_text_dict[word] += 1
            else:
                fake_text_dict[word] = 1
                
    for i in range(0, len(real_text)):
        title_words_r = real_title[i].split(' ')
        r = []
        for k in title_words_r:
            for j in k:
                if j in rmov:
                    k = k.replace(j," ")
            pli = k.split(" ")
            for b in pli:
                r.append(b)
            
        text_words_r = real_text[i].split(' ')
        for k in text_words_r:
            for j in k:
                if j in rmov:
                    k = k.replace(j," ")
            pli = k.split(' ')
            for b in pli:
                r.append(b)
            
        for word in r:
            if word in real_title_dict.keys():
                
            else:
                addWordCountInfoR(word, 1)
        for word in t:
            if word in real_text_dict.keys():
                real_text_dict[word] += 1
            else:
                addWordCountInfoR(word, 1)
 
def prevalency(article_dict, article_count):
    words_counts()
    high = 0
    low = list(article_dict.values())[0]
    total = 0
    copy = article_dict.copy()
    #loop through dictionary, make new dictionary with article count/word count for that word
    #at the same time find highest and lowest count of word to get range
    # get highest count/article, and lowest count/article
    # sum all word count per article
    # word count for one/total sum of word count for each word --> get that percent --> x 100 to return font size     
    for i in copy:
      if i.lower() in filler or i.upper() in filler:
          article_dict.pop(i)
    
    p = dict(list(article_dict.items()))
    op=""
    for i in p:
      p[i] = (p[i]/article_count)
      total += p[i]
      if p[i] > high:
          high = p[i]
      if p[i] < low:
          low = p[i]
         
    font_size = p.copy()
    diff = high - low
    rate = diff / 10
    
    
    
    for j in font_size:
      font_size[j] = (p[j]/high) * 100
      
    for j in font_size:
      if font_size[j] >= low and font_size[j] <= .0001:
          font_size[j] = 15
      if font_size[j] <= low:
          font_size[j] = 15
      elif font_size[j] > .0001 and font_size[j] <= .0002:
          font_size[j] = 20
      elif font_size[j] > .0002 and font_size[j] <= .0005:
          font_size[j] = 25
      elif font_size[j] > .0005 and font_size[j] <= .01:
          font_size[j] = 30
      elif font_size[j] > .01 and font_size[j] <= .03:
          font_size[j] = 40
      elif font_size[j] > .04 and font_size[j] <= .05:
          font_size[j] = 70
      elif font_size[j] > .05 and font_size[j] <= .2:
          font_size[j] = 70
      elif font_size[j] > .2 and font_size[j] <= .5:
          font_size[j] = 75
      elif font_size[j] > .5 and font_size[j] <= 1:
          font_size[j] = 75
      elif font_size[j] > low+(4*rate) and font_size[j] <= low + (5*rate):
          font_size[j] = 80
      elif font_size[j] > low+(5*rate) and font_size[j] <= low + (6*rate):
          font_size[j] = 80
      elif font_size[j] > low+(6*rate) and font_size[j] <= low + (7*rate):
          font_size[j] = 90
      elif font_size[j] > low+(7*rate) and font_size[j] <= low + (8*rate):
          font_size[j] = 90
      elif font_size[j] > low+(8*rate) and font_size[j] <= low + (9*rate):
          font_size[j] = 95
      elif font_size[j] > low+(9*rate) and font_size[j] <= low + (10*rate):
          font_size[j] = 100
      elif font_size[j] > low+(10*rate) and font_size[j] <= low + (11*rate):
          font_size[j] = 120
      else:
          font_size[j] = 20
    return font_size
          
def one():
    fake_article_count = len(fake)
    fake_article = prevalency(fake_text_dict, fake_article_count)
    deleteFontTableF()
    for i in dict(random.sample(list(fake_article.items()),25)):
        addFontSizeInfoF(i, fake_article[i])
    return returnFontTableF()


def fake_titles_words():
    deleteFontTableF()
    fake_title_count = len(fake)
    fake_title = prevalency(fake_title_dict, fake_title_count)
    return dict(random.sample(list(fake_title.items()),10))

def real_text_words():
    deleteFontTableR()
    real_article_count = len(real)
    real_article = prevalency(real_text_dict, real_article_count)
    for i in dict(random.sample(list(real_article.items()),25)):
        addFontSizeInfoR(i, real_article[i])
    return returnFontTableR()

    
def real_titles_words():
    real_title_count = len(real)
    real_title = prevalency(real_title_dict, real_title_count)
    return dict(random.sample(list(real_title.items()),10))




@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/dashboard")
def dashboard():
    if not 'username' in session:
        # add flash
        return redirect("/main")
    return render_template("dashboard.html")

@app.route("/search")
def search():
    if not 'username' in session:
        # add flash
        return redirect("/main")
    return render_template("search.html")

@app.route("/analyze")
def analyze():
    if not 'username' in session:
        # add flash
        return redirect("/main")
    return render_template("analyze.html")

@app.route("/generate")
def generate():
    if not 'username' in session:
        # add flash
        return redirect("/main")
    return render_template("generate.html")

if __name__ == "__main__":
    app.debug = True

    app.run()
