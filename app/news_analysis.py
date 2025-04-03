import numpy as np 
import pandas as pd 
import os 

fake = pd.read_csv(os.path.abspath('data/Fake (1).csv'))
real = pd.read_csv(os.path.abspath('data/True (1).csv'))

fake['true'] = 0
real['true'] = 1
news = pd.concat([fake, real], ignore_index = True)
#news.drop(['subject', 'date'], axis=1)
print(news.head(10))
def words_counts():
    fake_text = fake['text']
    fake_title = fake['title']
    real_text = real['text']
    real_title = real['title']
    fake_text_dict = {}
    fake_title_dict = {}
    
    real_text_dict = {}
    real_title_dict = {}
    for i in range(0, len(fake_text)):
        title_words = fake_title[i].split(' ')
        text_words = fake_text[i].split(' ')
        for word in title_words:
            if word in fake_title_dict.keys():
                fake_title_dict[word] += 1
            else:
                fake_title_dict[word] = 1
        for word in text_words:
            if word in fake_text_dict.keys():
                fake_text_dict[word] += 1
            else:
                fake_text_dict[word] = 1
    for i in range(0, len(real_text)):
        title_words = real_title[i].split(' ')
        text_words = real_text[i].split(' ')
        for word in title_words:
            if word in real_title_dict.keys():
                real_title_dict[word] += 1
            else:
                real_title_dict[word] = 1
        for word in text_words:
            if word in real_text_dict.keys():
                real_text_dict[word] += 1
            else:
                real_text_dict[word] = 1
<<<<<<< HEAD

def prevalency(article_dict, article_count):
    words_count()
    fake_article_count = len(fake)
    real_article_count = len(real)
    
    high = 0
    low = article_dict[0]
    sum = 0
    #loop through dictionary, make new dictionary with article count/word count for that word
    #at the same time find highest and lowest count of word to get range
    # get highest count/article, and lowest count/article
    # sum all word count per article
    # word count for one/total sum of word count for each word --> get that percent --> x 100 to return font size
    for i in fake_a:
      article_dict[i] = article_count / article_dict[i]
      sum += article_dict[i]
      if article_dict[i] > high:
          high = article_dict[i]
      if article_dict[i] < low:
          low = article_dict[i]
          
    
    
=======
    print(len(fake_text_dict))
words_counts()
>>>>>>> 62a874e516c4aad5ae6aaada95af687fa558f5e2
#prevalency
#for loop -- first word, check if any other wordsa in second loop (incrememnting by 1) is equal, add to count for that word, make key first i value, and value the count, move on to next key

    
