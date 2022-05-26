from textblob import TextBlob
import tweepy

# Twitter Keys
api_key = ""
api_key_secret = ""
access_token = ""
access_token_secret = ""

auth_handler = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
auth_handler.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth_handler) # Links to Twitter

# Twitter Search
search_term = 'guns'
tweet_amount = 100
tweets = tweepy.Cursor(api.search_tweets, q=search_term, lang="en").items(tweet_amount)

# Sentiment Analysis Variables
polarity = 0
positive = 0
neutral = 0
negative = 0

# Loop for tweets
for tweet in tweets:
    final_text = tweet.text.replace('RT', '')
    if final_text.startswith(' @'):
        position = final_text.index(":")
        final_text = final_text[position+2:]
    if final_text.startswith('@'):
        position = final_text.index(' ')
        final_text = final_text[position+2:]
    analysis = TextBlob(final_text)
    tweet_polarity = analysis.polarity
    if tweet_polarity > 0:
        positive += 1
    elif tweet_polarity < 0:
        negative += 1
    elif tweet_polarity == 0:
        neutral += 1
    polarity += tweet_polarity

# Print Tweets and Sentiment Analysis
print(polarity)
print(f'Amount of Positive Tweets: {positive}')
print(f'Amount of Neutral Tweets: {neutral}')
print(f'Amount of Negative Tweets: {negative}')
print(final_text) # Prints Tweets

