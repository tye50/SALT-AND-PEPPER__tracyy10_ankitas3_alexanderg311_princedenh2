# Fakeout | Fearless Dependent Journalism by SALT&PEPPER
Our website combs through a dataset of over 38,000 fake and true news articles to determine commonalities that are shared between them that may be used to predict other article’s trueness or falseness. The first page users will see is a page of randomized “bubbles” which each contain a word. Each bubble’s size will be proportional to the prevalence of that word throughout the dataset it was trained on while the color of the bubble will show whether the size is referring to the word’s prevalence in fake-news articles or true-news articles. Once the user is logged in, they will have access to more functions, including a search page where they can search a specific word and compare its appearances in fake vs. true articles, an analysis page where the user can input a link to an article on the web and a rating of real or fake will be returned with an analysis of metrics used to reach the conclusion, and lastly a page that allows the user to generate an article that contains either fake or real news related to their inputted word (super stretch goal).

Added ability for users to write their own blocks of text to be rated “true” or “false.” Rather than being assigned a boolean true or false value, each article is rather given a score (some real number from 0 to 1) determining its truth value. This will turn our model from discrete to continuous, further allowing one to better understand the outputted data and allowing one to draw larger conclusions. 

## Roster & Roles
Tracy Ye - Project Manager & DB <br />
Ankita Saha - Data Visualization/Cleaning & FEF (Bootstrap) <br />
Sascha Gordon-Zolov - Flask person <br />
Princeden H. - Pytorch/Data Classification <br />

## Install Guide
1. Clone this repo
```
$ git clone git@github.com:tye50/SALT-AND-PEPPER__tracyy10_ankitas3_alexanderg311_princedenh2.git
```
3. Navigate into the cloned repo
```
$ cd SALT-AND-PEPPER__tracyy10_ankitas3_alexanderg311_princedenh2
```
4. Create a virtual environment
```
$ python3 -m venv foo
```
5. Activate your virtual environment
```
$ . foo/bin/activate
```
6. Install the packages required to run this program
```
$ pip install -r requirements.txt
```

## Launch Codes
1. Navigate into the cloned repo
```
$ cd SALT-AND-PEPPER__tracyy10_ankitas3_alexanderg311_princedenh2
```
3. Launch the app
```
$ python3 app/__init__.py
```
5. Click on the link printed in your terminal
```
http://127.0.0.1:5000
```

## Alternative Launch Code
1. Follow this link!
```
http://138.197.96.116:5000
```
