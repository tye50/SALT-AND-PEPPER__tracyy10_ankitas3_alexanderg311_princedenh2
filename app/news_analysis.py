import numpy as np 
import pandas as pd 
import os

fake = pd.read_csv(os.path.abspath('data/Fake (1).csv'))
real = pd.read_csv(os.path.abspath('data/True (1).csv'))

# default = spacy.load("en_core_web_lg")
# filler = en.Defaults.stop_words
filler = {'call', 'upon', 'still', 'nevertheless', 'down', 'every', 'forty', '‘re', 'always', 'whole', 'side', "n't", 'now', 'however', 'an', 'show', 'least', 'give', 'below', 'did', 'sometimes', 'which', "'s", 'nowhere', 'per', 'hereupon', 'yours', 'she', 'moreover', 'eight', 'somewhere', 'within', 'whereby', 'few', 'has', 'so', 'have', 'for', 'noone', 'top', 'were', 'those', 'thence', 'eleven', 'after', 'no', '’ll', 'others', 'ourselves', 'themselves', 'though', 'that', 'nor', 'just', '’s', 'before', 'had', 'toward', 'another', 'should', 'herself', 'and', 'these', 'such', 'elsewhere', 'further', 'next', 'indeed', 'bottom', 'anyone', 'his', 'each', 'then', 'both', 'became', 'third', 'whom', '‘ve', 'mine', 'take', 'many', 'anywhere', 'to', 'well', 'thereafter', 'besides', 'almost', 'front', 'fifteen', 'towards', 'none', 'be', 'herein', 'two', 'using', 'whatever', 'please', 'perhaps', 'full', 'ca', 'we', 'latterly', 'here', 'therefore', 'us', 'how', 'was', 'made', 'the', 'or', 'may', '’re', 'namely', "'ve", 'anyway', 'amongst', 'used', 'ever', 'of', 'there', 'than', 'why', 'really', 'whither', 'in', 'only', 'wherein', 'last', 'under', 'own', 'therein', 'go', 'seems', '‘m', 'wherever', 'either', 'someone', 'up', 'doing', 'on', 'rather', 'ours', 'again', 'same', 'over', '‘s', 'latter', 'during', 'done', "'re", 'put', "'m", 'much', 'neither', 'among', 'seemed', 'into', 'once', 'my', 'otherwise', 'part', 'everywhere', 'never', 'myself', 'must', 'will', 'am', 'can', 'else', 'although', 'as', 'beyond', 'are', 'too', 'becomes', 'does', 'a', 'everyone', 'but', 'some', 'regarding', '‘ll', 'against', 'throughout', 'yourselves', 'him', "'d", 'it', 'himself', 'whether', 'move', '’m', 'hereafter', 're', 'while', 'whoever', 'your', 'first', 'amount', 'twelve', 'serious', 'other', 'any', 'off', 'seeming', 'four', 'itself', 'nothing', 'beforehand', 'make', 'out', 'very', 'already', 'various', 'until', 'hers', 'they', 'not', 'them', 'where', 'would', 'since', 'everything', 'at', 'together', 'yet', 'more', 'six', 'back', 'with', 'thereupon', 'becoming', 'around', 'due', 'keep', 'somehow', 'n‘t', 'across', 'all', 'when', 'i', 'empty', 'nine', 'five', 'get', 'see', 'been', 'name', 'between', 'hence', 'ten', 'several', 'from', 'whereupon', 'through', 'hereby', "'ll", 'alone', 'something', 'formerly', 'without', 'above', 'onto', 'except', 'enough', 'become', 'behind', '’d', 'its', 'most', 'n’t', 'might', 'whereas', 'anything', 'if', 'her', 'via', 'fifty', 'is', 'thereby', 'twenty', 'often', 'whereafter', 'their', 'also', 'anyhow', 'cannot', 'our', 'could', 'because', 'who', 'beside', 'by', 'whence', 'being', 'meanwhile', 'this', 'afterwards', 'whenever', 'mostly', 'what', 'one', 'nobody', 'seem', 'less', 'do', '‘d', 'say', 'thus', 'unless', 'along', 'yourself', 'former', 'thru', 'he', 'hundred', 'three', 'sixty', 'me', 'sometime', 'whose', 'you', 'quite', '’ve', 'about', 'even'}

fake['true'] = 0
real['true'] = 1
news = pd.concat([fake, real], ignore_index = True)
#news.drop(['subject', 'date'], axis=1)
# print(news.head(10))

fake_text = fake['text']
fake_title = fake['title']
real_text = real['text']
real_title = real['title']
fake_text_dict = {}
fake_title_dict = {}

real_text_dict = {}
real_title_dict = {}
    
def words_counts():
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
 
def prevalency(article_dict, article_count):
    high = 0
    low = article_dict[0]
    sum = 0
    #loop through dictionary, make new dictionary with article count/word count for that word
    #at the same time find highest and lowest count of word to get range
    # get highest count/article, and lowest count/article
    # sum all word count per article
    # word count for one/total sum of word count for each word --> get that percent --> x 100 to return font size
    for i in article_dict:
      if i in filler:
          article_dict.pop(i)
          
    for i in article_dict:
      article_dict[i] = article_count / article_dict[i]
      sum += article_dict[i]
      if article_dict[i] > high:
          high = article_dict[i]
      if article_dict[i] < low:
          low = article_dict[i]
         
    font_size = article_dict.copy()
    
    for j in font_size:
      font_size[j] = (article_dict[i]/high) * 100
    return font_size
          
def one():
    words_count()
    
    fake_article_count = len(fake)
    fake_article = prevalency(fake_text_dict, fake_article_count)
    
    return fake_article[:10]
    
def get_font_sizes():
    words_count()
    
    fake_article_count = len(fake)
    fake_article = prevalency(fake_text_dict, fake_article_count)
    
    real_article_count = len(real)
    real_article = prevalency(real_text_dict, real_article_count)
    
    fake_title_count = len(fake)
    fake_title = prevalency(fake_title_dict, fake_title_count)
    
    real_title_count = len(real)
    real_title = prevalency(real_title_dict, real_title_count)
    


