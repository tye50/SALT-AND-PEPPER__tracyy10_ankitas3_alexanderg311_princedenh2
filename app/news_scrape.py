import requests
from bs4 import BeautifulSoup
from newspaper import Article

url = 'https://www.theatlantic.com/international/archive/2025/04/wayne-gretzky-canadian-hero/682322/?utm_source=firefox-newtab-en-us'
article = Article(url)
article.download()
article.parse()
	# Extract and print the desired data
print("**Headline:**", article.title)
print("**Authors:**", article.authors)
print("**Publication Date:**", article.publish_date)
print("**Main Text:**", article.text)


