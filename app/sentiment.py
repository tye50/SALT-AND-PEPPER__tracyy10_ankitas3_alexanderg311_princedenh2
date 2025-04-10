# https://text2data.com/Integration 
# https://github.com/shabisht/Sentiment-Analysis-API
# https://cloud.google.com/natural-language/docs/analyzing-sentiment#language-sentiment-string-python

import requests # pip install requests
import urllib.request
import urllib.parse
import json

url='http://api.text2data.com/v3/analyze'
payload={
    'DocumentText': 'Excellent location, opposite a very large mall with wide variety of shops, restaurants and more.',
    'IsTwitterContent': 'false',
    'PrivateKey': 'D746EA6F-87A2-42A4-876D-A070B8D27693',
    'Secret':'salty'
    }

r = requests.post(url, data=payload)
data=r.json()
 
if data['Status'] == 1:
   print('This document is: %s%s %+.2f' % (data['DocSentimentPolarity'], data['DocSentimentResultString'],data['DocSentimentValue']))
   print('Magnitude: %.2f' %(data['Magnitude']))
   print('Subjectivity: %s' %(data['Subjectivity']))
 
   print('Themes')
 
   for item in data['Themes']:
     print('%s (%s) %s%s %+.2f' %(item['Text'], item['KeywordType'], item['SentimentPolarity'], item['SentimentResult'], item['SentimentValue']))
 
   print('Entities')
 
   for item in data['Entities']:
     print('%s (%s) %s%s %+.2f' %(item['Text'], item['KeywordType'], item['SentimentPolarity'], item['SentimentResult'], item['SentimentValue']))
 
   print('Keywords')
 
   for item in data['Keywords']:
     print('%s (%s) %s%s %+.2f' %(item['Text'], item['KeywordType'], item['SentimentPolarity'], item['SentimentResult'], item['SentimentValue']))
 
else: 
   print(data['ErrorMessage'])