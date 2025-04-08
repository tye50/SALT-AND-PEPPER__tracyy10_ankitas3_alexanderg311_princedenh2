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
    print(real_text_dict['the'])
words_counts()
#prevalency
#for loop -- first word, check if any other wordsa in second loop (incrememnting by 1) is equal, add to count for that word, make key first i value, and value the count, move on to next key

