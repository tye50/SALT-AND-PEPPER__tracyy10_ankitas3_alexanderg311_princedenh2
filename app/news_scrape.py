import requests
from newspaper import Article

def get_text(url):
	article = Article(url)
	article.download()
	article.parse()
		# Extract and print the desired data
	return article.title + article.text

