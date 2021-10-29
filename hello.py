from mediawiki import MediaWiki

wikipedia = MediaWiki()
you = wikipedia.page("You(TV series)")
print(you.title)
print(you.content)

### Natural Language Processing
#part of speech tagging


#sentiment analysis
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon') #error in line 8 told me to add this line of code to get my score to work

x = you.split()
score = SentimentIntensityAnalyzer().polarity_scores(x)
print(score)

#results: {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}