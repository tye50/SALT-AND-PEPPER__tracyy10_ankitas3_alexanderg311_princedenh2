# Fakeout | Fearless Dependent Journalism by SALT&PEPPER
Our website combs through a dataset of over 38,000 fake and true news articles to determine commonalities that are shared between them that may be used to predict other article’s trueness or falseness. The first page users will see is a page of randomized words that vary in size and color. Each word’s size will be proportional to the occurrence rate of that word throughout the dataset it was trained on while the color of the bubble will show whether the size is referring to the word’s prevalence in fake-news articles or true-news articles. Once the user is logged in, they will have access to more functions, including a search page where they can find a specific word and compare its appearances in fake vs. true articles and an analysis page where the user can input a link to an article on the web and a rating of real or fake will be returned along with a judgement on the objectivity and tone of the article  and keywords that helped in making the decision.

## Roster & Roles
Tracy Ye - Project Manager & DB & API<br />
Ankita Saha - Data Visualization/Cleaning & FEF (Bootstrap) <br />
Sascha Gordon-Zolov - Flask person & CSS <br />
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
http://salt.tye50.tech/
```

### FEATURE SPOTLIGHT
* Check out Sascha and Princeden's news_classifier.py created with scikit
* Read the how-to at https://github.com/stuy-softdev/notes-and-code/blob/main/kb/how-to/howto_scikit.md
* This article was used to test the analyze page (both the API and the trained model returned many interesting values): https://www.bbc.com/news/articles/c4g8ry3x172o
* Or try inserting an Onion article!

### KNOWN BUGS/ISSUES
* The Text2Data api offers very few transactions per account, so the website's version will likely not work and cause an "Invalid URL" error (flash message). To work around this, clone the repository locaclly and fill the private key and secret key values in with your own (provisioning an account is very convenient).
* Alas, the generate streatch goal was never reached