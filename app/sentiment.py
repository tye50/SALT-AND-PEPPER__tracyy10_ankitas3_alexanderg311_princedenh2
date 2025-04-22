# https://text2data.com/Integration 
# https://github.com/shabisht/Sentiment-Analysis-API
# https://cloud.google.com/natural-language/docs/analyzing-sentiment#language-sentiment-string-python

import requests # pip install requests
import urllib.request
import urllib.parse
import json

url='http://api.text2data.com/v3/analyze'
payload={
    'DocumentText': 'The Department of Education will resume collections on defaulted student loans on May 5, it said on Monday, warning that borrowers could be referred to debt collectors or enrolled in income-based repayment plans.The federal government paused repayment requirements on student loan debt in March 2020, in the midst of the coronavirus pandemic. Borrowers whose student loans were in forbearance have not had to make payments since then.President Joseph R. Biden Jr. repeatedly sought during his administration to bring defaulted student loan borrowers back into good standing, or to erase their debt entirely. Plans to forgive up to $20,000 in loans for millions of borrowers were struck down by the Supreme Court, and a Biden-era repayment plan known as SAVE — which would adjust borrowers’ payment plans based on household size and income — has been frozen by the court since August.The Trump White House has long telegraphed that no such concessions would be offered for student loan holders under its administration.',
    'IsTwitterContent': 'false',
    'PrivateKey': '878A17EC-4798-4680-AE46-8A4DD7482F0B',
    'Secret':'eat'
    }

r = requests.post(url, data=payload)
data=r.json()
 
if data['Status'] == 1:
   print('This document is: %s%s %+.2f' % (data['DocSentimentPolarity'], data['DocSentimentResultString'],data['DocSentimentValue']))
   print('Magnitude: %.2f' %(data['Magnitude']))
   print('Subjectivity: %s' %(data['Subjectivity']))
   print()
   
   print('################ Themes ################')
   for item in data['Themes']:
     print('%s (%s) %s%s %+.2f %s' %(item['Text'], item['KeywordType'], item['SentimentPolarity'], item['SentimentResult'], item['SentimentValue'], item['Mentions']))
   print()
   
   print('################ Entities ################')
   for item in data['Entities']:
     print('%s (%s) %s%s %+.2f' %(item['Text'], item['KeywordType'], item['SentimentPolarity'], item['SentimentResult'], item['SentimentValue']))
   print()
   
   print('################ Keywords ################')
   for item in data['Keywords']:
     print('%s (%s) %s%s %+.2f' %(item['Text'], item['KeywordType'], item['SentimentPolarity'], item['SentimentResult'], item['SentimentValue']))

else: 
   print(data['ErrorMessage'])
   



# {
#   "DocSentimentResultString": "string",
#   "DocSentimentValue": 0,
#   "DocSentimentPolarity": "string",
#   "Magnitude": 0,
#   "Entities": [
#     {
#       "Text": "string",
#       "SentenceText": "string",
#       "Mentions": 0,
#       "Magnitude": 0,
#       "SentencePartType": "string",
#       "KeywordType": "string",
#       "SentimentResult": "string",
#       "SentimentValue": 0,
#       "SentimentPolarity": "string"
#     }
#   ],
#   "Themes": [
#     {
#       "Text": "string",
#       "SentenceText": "string",
#       "Mentions": 0,
#       "Magnitude": 0,
#       "SentencePartType": "string",
#       "KeywordType": "string",
#       "SentimentResult": "string",
#       "SentimentValue": 0,
#       "SentimentPolarity": "string"
#     }
#   ],
#   "Keywords": [
#     {
#       "Text": "string",
#       "SentenceText": "string",
#       "Mentions": 0,
#       "Magnitude": 0,
#       "SentencePartType": "string",
#       "KeywordType": "string",
#       "SentimentResult": "string",
#       "SentimentValue": 0,
#       "SentimentPolarity": "string"
#     }
#   ],
#   "Citations": [
#     {
#       "Text": "string",
#       "SentenceText": "string",
#       "Mentions": 0,
#       "Magnitude": 0,
#       "SentencePartType": "string",
#       "KeywordType": "string",
#       "SentimentResult": "string",
#       "SentimentValue": 0,
#       "SentimentPolarity": "string"
#     }
#   ],
#   "SlangWords": [
#     {
#       "SlangWordText": "string",
#       "SlangWordTranslation": "string"
#     }
#   ],
#   "SwearWords": [
#     {
#       "SlangWordText": "string",
#       "SlangWordTranslation": "string"
#     }
#   ],
#   "CoreSentences": [
#     {
#       "SentenceNumber": 0,
#       "Text": "string",
#       "SentimentResultString": "string",
#       "SentimentValue": 0,
#       "SentimentPolarity": "string",
#       "Relevance": 0,
#       "Magnitude": 0
#     }
#   ],
#   "PartsOfSpeech": [
#     {
#       "Text": "string",
#       "Subject": "string",
#       "Action": "string",
#       "Object": "string",
#       "ObjectSentimentResultString": "string",
#       "ObjectSentimentValue": 0,
#       "ObjectSentimentPolarity": "string"
#     }
#   ],
#   "AutoCategories": [
#     {
#       "CategoryName": "string",
#       "Score": 0
#     }
#   ],
#   "UserCategories": [
#     {
#       "CategoryName": "string",
#       "Score": 0
#     }
#   ],
#   "Subjectivity": "string",
#   "DetectedLanguage": "string",
#   "ErrorMessage": "string",
#   "Status": 0,
#   "TransactionTotalCreditsLeft": 0,
#   "TransactionUseByDate": "2019-04-22T11:32:21.332Z",
#   "TransactionCurrentDay": 0,
#   "TransactionDailyLimit": 0
# }
# 
# '''
#   "DocSentimentResultString": "string",
#   "DocSentimentValue": 0,
#   "DocSentimentPolarity": "string",
#   "Magnitude": 0,
#   "Entities": [
#     {
#       "Text": "string",
#       "SentenceText": "string",
#       "Mentions": 0,
#       "Magnitude": 0,
#       "SentencePartType": "string",
#       "KeywordType": "string",
#       "SentimentResult": "string",
#       "SentimentValue": 0,
#       "SentimentPolarity": "string"
#     }
#   ],
#   "Themes": [
#     {
#       "Text": "string",
#       "SentenceText": "string",
#       "Mentions": 0,
#       "Magnitude": 0,
#       "SentencePartType": "string",
#       "KeywordType": "string",
#       "SentimentResult": "string",
#       "SentimentValue": 0,
#       "SentimentPolarity": "string"
#     }
#   ],
#   "Keywords": [
#     {
#       "Text": "string",
#       "SentenceText": "string",
#       "Mentions": 0,
#       "Magnitude": 0,
#       "SentencePartType": "string",
#       "KeywordType": "string",
#       "SentimentResult": "string",
#       "SentimentValue": 0,
#       "SentimentPolarity": "string"
#     }
#   ],
#   "Citations": [
#     {
#       "Text": "string",
#       "SentenceText": "string",
#       "Mentions": 0,
#       "Magnitude": 0,
#       "SentencePartType": "string",
#       "KeywordType": "string",
#       "SentimentResult": "string",
#       "SentimentValue": 0,
#       "SentimentPolarity": "string"
#     }
#   ],
#   "SlangWords": [
#     {
#       "SlangWordText": "string",
#       "SlangWordTranslation": "string"
#     }
#   ],
#   "SwearWords": [
#     {
#       "SlangWordText": "string",
#       "SlangWordTranslation": "string"
#     }
#   ],
#   "CoreSentences": [
#     {
#       "SentenceNumber": 0,
#       "Text": "string",
#       "SentimentResultString": "string",
#       "SentimentValue": 0,
#       "SentimentPolarity": "string",
#       "Relevance": 0,
#       "Magnitude": 0
#     }
#   ],
#   "PartsOfSpeech": [
#     {
#       "Text": "string",
#       "Subject": "string",
#       "Action": "string",
#       "Object": "string",
#       "ObjectSentimentResultString": "string",
#       "ObjectSentimentValue": 0,
#       "ObjectSentimentPolarity": "string"
#     }
#   ],
#   "AutoCategories": [
#     {
#       "CategoryName": "string",
#       "Score": 0
#     }
#   ],
#   "UserCategories": [
#     {
#       "CategoryName": "string",
#       "Score": 0
#     }
#   ],
#   "Subjectivity": "string",
#   "DetectedLanguage": "string",
#   "ErrorMessage": "string",
#   "Status": 0,
#   "TransactionTotalCreditsLeft": 0,
#   "TransactionUseByDate": "2019-04-22T11:32:21.332Z",
#   "TransactionCurrentDay": 0,
#   "TransactionDailyLimit": 0

