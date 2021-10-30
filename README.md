# Ziyuan Zhu - Text Mining Assignment

# Project Overview
From part 1, I found my data source from Project Gutenberg, specifically, A Apple Pie by Kate Greenaway. For this data source, I used two techniques: characterizing by word frequencies and computing summary statistics. My goal was to use a dictionary and calculate frequencies of words in the text. Another goal I had was to figure out the top 10 words in the text.
Another data source that I pulled was from Wikipedia. I wanted to analyze the page for You, which is a Netflix-hit television show. For this data source, I used Natural Language Processing. My goal was to create sentiment analysis and evaluate the results. 

# Implementation 
For the first data source, I chose to analyze the top ten words from the text because it was a children’s book and I assumed that there were not a lot of words that would be written. For the data structure, I had to first establish the text, split it in order to count the frequency of each words and added the result in an empty dictionary. 

For the second data source, I thought it would be interesting to analyze a summary on wikipedia on a murderous - crime show. I chose sentiment analysis as my design technique because I was curious to see if the results would be mostly neutral or negative. I hypothesized that because there are words such as killer, murder, and death, it would have more of a negative result. However, because the summary is an objective, third person point of view narration, I thought it would also be possible that the results were neutral. A major component that I had to import was “import nltk” and “import SentimentIntensityAnalyzer” in order to conduct the analysis. When I ran my code, there was an error in the output that wanted me to add “nltk.download('vader_lexicon')” in my code. This was something that still confuses me because after doing research, the line’s purpose was a tool that is specifically attuned to sentiments expressed in social media. I was wondering 

# Results
For the Project Gutenberg data source, I was able to compute the frequency of each word in the text as well as sorting the top 10 most frequent words that appeared in the text. When computing the frequency of each word in the book, I was initially surprised that there were so many words for a mere children’s alphabet book. Then, I realized that there was a lot of excess information in the beginning and end of the book, which was not the result I had hoped for. Another thing that was really interesting was that the top 10 words weren’t nouns, verbs or adjectives. It was mostly article words and conjunction words. 

For the Wikipedia data source, I was able to conduct a sentiment analysis. I thought this was an interesting technique to use because even though Wikipedia showcased facts about the TV show, it still had positive, neutral, negative and compound calculations of 0.123, 0.719, 0.158, and 0.4939. I was surprised to see the results of the text weren’t considered only neutral as it was a summary of a television show. 

# Reflection
For the first data source, I struggled a lot in terms of filtering my book from Project Gutenberg. The book I chose to analyze was a book that taught children the alphabet. However, there was a lot of excess information located in the beginning and end of the book that I hoped to filter out. This definitely skewed my calculations as it had a lot more data than it should. Going forward, I would like to learn how to effectively filter out certain unnecessary information. Overall, it was not a hard task since I am familiar with the dictionary from learning in class. 

For the second data source, I initially struggled a lot with running the command prompt. However, I was able to figure out that I had installed two Python’s, in which I got rid of the one downloaded from the Microsoft store. Although it was a little hard to grasp the concept of Natural Language Processing at first, I was able to conduct sentiment analysis. I could have improved in choosing a better data source, such as IMDB reviews, for this method because analyzing a summary may be inaccurate. 
