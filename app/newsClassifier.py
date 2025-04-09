import numpy as np 
import pandas as pd 
import os
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score

from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import pickle
from sklearn.naive_bayes import GaussianNB

fake = pd.read_csv(os.path.abspath('data/Fake (1).csv'))
real = pd.read_csv(os.path.abspath('data/True (1).csv'))

fake['true'] = 0
real['true'] = 1
news = pd.concat([fake, real], ignore_index = True)
news.drop(['subject', 'date'], axis=1, inplace=True)

x = news[['title', 'text']]
y = news['true']
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
tfidf_vectorizer = TfidfVectorizer()
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train["title"] + " " + X_train["text"])

X_test_tfidf = tfidf_vectorizer.transform(X_test["title"] + " " + X_test["text"])





model = MultinomialNB()

model.fit(X_train_tfidf, y_train)
y_pred = model.predict(X_test_tfidf)
accuracy = accuracy_score(y_test, y_pred)
print(f"{model.__class__.__name__}: {accuracy*100:.2f}")
print("-"*30)
filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, y_test)
print(result)
def predict(text):
    prediction = model.predict(tfidf_vectorizer.transform(["""" 

Layoffs, price hikes, retaliation: What workers can expect from Trump’s trade war
April 3, 2025	12:51 PM CDT By C.J. Atkins
Layoffs, price hikes, retaliation: What workers can expect from Trump’s trade war	
'Liberation Day': Trump declares economic war against the whole world - and against U.S. workers - at his White House tariff theater performance on April 2. | AP

    Click here for more People’s World articles on Trade and Tariffs.

 

Just a sampling of headlines on the first day of the USA’s new “Golden Age” serves to illustrate the chaos and uncertainty – along with the ridiculousness and absurdity – of President Donald Trump’s post-globalization world.

    “Layoff announcements surge to the most since the pandemic.”
    “Stock market tumbles 1,000 1,200 1,300 1,500 1,600 points on fear Trump’s tariffs will spark trade war.”
    “Even if it’s made in the USA, they will jack up the price and blame it on tariffs.”
    “Cars were already unaffordable before tariffs.”
    “‘What extraordinary nonsense’: Trump’s tariff math is crazy.”
    “Trump’s tariffs are truly global – Just ask the penguins of McDonald Islands.”

And these are just things the bourgeois press and corporate commentators – in outlets like CNBC, the Wall Street Journal, and Politico – have to say about the situation.

Stock markets have cratered and countries around the globe are threatening retaliation in response to the declaration of economic warfare unveiled by Trump during his “Liberation Day” circus at the White House on April 2.

As People’s World noted two months ago, what we’re witnessing in real-time is a struggle within the ruling class over what the future of U.S. capitalism – in fact, world capitalism – should look like.

Representing those sectors of capital feeling the heat of competition on the world market (especially from China’s rapidly advancing firms), Trump has the system of free trade in his crosshairs. Arrayed against him – as illustrated in the headlines above – are those capitalists and neoliberal ideologues who remain as committed as ever to the system of free trade and open markets.
A trader on the floor of the New York Stock Exchange reacts as he watches share prices plummet on the morning of April 3. | AP

But erecting protectionist walls around particular U.S. corporations and hurting foreign manufacturers isn’t Trump’s only goal. This whole tariff onslaught has another aim in mind: Making the American working class pay for the next round of tax cuts he wants to give to corporations and billionaires.

His economic advisors are betting (hoping? naively wishing?) that the revenues from his tariffs will fill the U.S. Treasury’s coffers with so much cash that the government will be able to afford another giant tax cut for the rich and perhaps even eliminate income taxes altogether.

Who pays?

But the question Trump and his spokespeople always try to avoid: Who pays the tariffs?

The White House occupant is constantly saying things like, “China will pay,” “Vietnam can’t take advantage of us anymore,” “Canada will have to stop cheating us.” As has been pointed out repeatedly, though, tariffs aren’t paid by foreign companies or governments. They are import taxes paid by U.S. companies who bring in foreign-made goods, and those companies will inevitably pass much of that tax on to their customers, which means all of us.

It’s trickle-down economics of a different kind. We pay more so that Trump can afford another round of giveaways to the super-rich.

Shoes, toys, household goods, appliances, electronics, cars, building materials, imported produce – all these things are going to cost us more, and in some cases a lot more. When you go to the dollar store, to the grocery store, to the car dealership, to the lumberyard, prepare for some sticker shock in the coming weeks and months.

The administration is trying to distract and paper over this reality. They want working-class and poor people to be dazzled by predictions of new jobs, more factories, and better wages. As Trump told the nation a few weeks ago: “We will take in trillions of dollars and create jobs like we’ve never seen before.” But it’s a sham promise.

Slapping a pro-labor façade on protectionist policies is a time-worn tactic. The same game has been played by bosses forever. They try to get their workers to identify with the company and compete with other companies and other workers. Trump’s doing the same thing at a national level. We’re all on the same team here, don’t you know?

His staff sprinkled a few union workers among the small crowd at his trade war theater performance on April 2 to make the point. Men wearing hard hats plastered with United Steel Workers decals were positioned directly in front of television cameras for maximum effect.

The reality for the working class is going to be a period of inflationary prices, however, with no guarantees that the president’s promises of new jobs and reopened factories will ever be fulfilled.

Trade War 2.0

We’ve been here before.

In 2018, Trump launched a smaller-scale version of what’s happening now – a trade war dress rehearsal, mostly targeting China. The explanation he gave at the time, and which might have sounded appealing to many workers, is that the U.S. would make money from Chinese tariff payments and more jobs would be created within the U.S. in the long run.

As we’ve said, however, that’s not how tariffs work, and it’s not what happened.

An in-depth study by the experts at the Economic Policy Institute in 2020 surveyed the results of the tariff wars of the first MAGA presidency. Their conclusion: Trump’s trade policies cost thousands of U.S. manufacturing jobs. When he was president for the first time, more than 1,800 factories disappeared from the U.S., and there was a net loss of manufacturing jobs.
The still-idled and crumbling Republic Steel mill in Lorain, Ohio. | Photo via City of Lorain

Capitalists played their part in the deceptive effort to sell the trade war, though. Seven years ago, Republic Steel bosses stood at Trump’s side and said that thanks to his steel tariffs, they’d be reopening their Lorain, Ohio plant, bringing back 1,000 jobs.

It never happened. The industrial renaissance, the new “Golden Age,” never came to Lorain.

Instead of bringing jobs, the main thing Trump’s earlier tariffs accomplished was raising prices for U.S. consumers, ranging from 1.7% to 7.1%, depending on the sector. In 2018 alone, UCLA researchers calculated that every single person in the country paid on average an extra $213 in indirect import taxes.

And the real kicker for those who believed Trump’s trade rhetoric? Workers and farmers in heavily Republican counties were the most negatively affected by the trade war. As one group of analysts put it, there was “no help for the Heartland.”

This time will be worse. The Center for American Progress has crunched the numbers and projects that Trump’s new tariffs could cost American households $5,200 annually, but they are “unlikely to create jobs, improve U.S. economic competitiveness, or improve America’s standing in the world.”

Even Mike Pence (of Jan. 6th “Hang Mike Pence” fame) is alleging the tariffs will suck at least $3,500 a year out of workers’ wallets. He’s warning fellow Republicans that the trade war “could cost American families thousands of dollars, destroy American jobs, and potentially lose conservatives their governing majority.”

And in a rare admission from one of the dissident voices among the ruling class, Wall Street financier Mark Cuban is urging people to prepare for price-gouging even on things not impacted by tariffs. He’s advising everyone to rush to stores and stock up on everything from toothpaste to soap. “Even if it’s made in the USA,” he said in a BlueSky post, “they will jack up the price and blame it on tariffs.”

All these damaging impacts and we haven’t even talked about the retaliatory tariffs that other countries are sure to put on U.S.-made goods. The first big round of layoffs already started. Less than 24 hours after Trump’s announcement, Stellantis shuttered several of its powertrain and stamping facilities, terminating at least 900 workers for the time being. The layoffs will hit workers at the Warren and Sterling Heights stamping plants in Michigan and the company’s transmission and casting plants in Indiana. Across the border in Ontario, some 6,000 auto assembly and parts plant workers were handed layoff notices, put on furlough while companies assess the impact of the tariffs.

Compromise and negotiation between nations over trade is the only way forward, and the tit-for-tat imposition of tariffs by the Trump administration and other governments is not going to benefit working people anywhere.

The White House, MAGA ideologues, and the right-wing media are trying to entice us with promises of a stronger U.S. economy and assuring us that the “adjustment period” of increased costs will be short-lived.

But when have you known Donald Trump to tell the truth about anything?

As with all op-eds, this article reflects the views of its author.
"""]))
print(prediction)
