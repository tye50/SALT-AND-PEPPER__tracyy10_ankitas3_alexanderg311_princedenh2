import requests # pip install requests
import urllib.request
import urllib.parse
import json

def text2data(text):
    url='http://api.text2data.com/v3/analyze'
    payload={
        'DocumentText': {text},
        'IsTwitterContent': 'false',
        'PrivateKey': 'DA9E28ED-1D0F-4997-B59C-A27A778D4C55',
        'Secret':'salty'
        }

    r = requests.post(url, data=payload)
    data=r.json()
     
    if data['Status'] == 1:
        ret = dict()
        ret["Sentiment"]='%s %+.3f' %(data['DocSentimentResultString'], data['DocSentimentValue'])
        ret["Magnitude"]='%.3f' %(data['Magnitude'])
        ret["Objectivity"]='%s' %(data['Subjectivity'])
        
        theme=[]
        for item in data['Themes']:
            theme.append(['%s' %item['Text'], '%s' %item['SentimentResult'], '%+.3f' %item['SentimentValue'], '%s' %item['Mentions']])
            #                        phrase              pos/neg                             magnitude                   occurances
        ret["Theme"]=theme
        
        keywords=[]
        for item in data['Keywords']:
            keywords.append(['%s' %item['Text'], '%s' %item['SentenceText'], '%s' %item['SentimentResult'], '%+.3f' %item['SentimentValue'], '%s' %item['Mentions']])
            #                        phrase              senetence it belonged            pos/neg                           magnitude                   occurances
        ret["Keywords"]=keywords
        
        return ret # return dictionary
    else: 
        return 0 # error returned
