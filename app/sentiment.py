import requests # pip install requests
import urllib.request
import urllib.parse
import json

def text2data(text):
    url='http://api.text2data.com/v3/analyze'
    payload={
        'DocumentText': {text},
        'IsTwitterContent': 'false',
        'PrivateKey': '878A17EC-4798-4680-AE46-8A4DD7482F0B',
        'Secret':'eat'
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
    
print(text2data("The Department of Education will resume collections on defaulted student loans on May 5, it said on Monday, warning that borrowers could be referred to debt collectors or enrolled in income-based repayment plans.The federal government paused repayment requirements on student loan debt in March 2020, in the midst of the coronavirus pandemic. Borrowers whose student loans were in forbearance have not had to make payments since then.President Joseph R. Biden Jr. repeatedly sought during his administration to bring defaulted student loan borrowers back into good standing, or to erase their debt entirely. Plans to forgive up to $20,000 in loans for millions of borrowers were struck down by the Supreme Court, and a Biden-era repayment plan known as SAVE — which would adjust borrowers’ payment plans based on household size and income — has been frozen by the court since August.The Trump White House has long telegraphed that no such concessions would be offered for student loan holders under its administration."))