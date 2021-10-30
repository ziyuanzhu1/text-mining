from mediawiki import MediaWiki

wikipedia = MediaWiki()
you = wikipedia.page("You(TV series)")
print(you.title)
print(you.content)

### Natural Language Processing
#sentiment analysis
import nltk 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon') #error in line 8 told me to add this line of code to get my score to work
sentence = 'On the review aggregator website, Rotten Tomatoes, the first season has a 93 percent approval rating with 60 reviews, with an average rating of 7.10/10. The websites critical consensus reads, "You pairs thrilling drama with trashy fun to create an addictive social media horror story that works its way under the skin – and stays there." Review aggregator Metacritic gave the first season a normalized score of 74 out of 100 based on 29 critics, indicating "generally favorable reviews'
score = SentimentIntensityAnalyzer().polarity_scores(sentence)
print(score)

#results: {'neg': 0.0, 'neu': 1.0, 'pos': 0.0, 'compound': 0.0}