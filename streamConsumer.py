from kafka import KafkaConsumer
import re
from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext
import json
from textblob import TextBlob



def clean_tweet(tweet):
	'''
	Function to remove emoticons and other non textual data from the tweet
        '''

	return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


# def get_sentiment(tweet_json):
#
#     result = TextBlob(tweet_json)
#
#     sentiment_polarity = result.sentiment.polarity
#
#     if (sentiment_polarity > 0):
#         result = result + ' - positive'
#         return result
#     elif (sentiment_polarity == 0):
#         result = result + ' - neutral'
#         return result
#     else:
#         result = result + ' - negative'
#         return result

def main():
    '''
    Consumer consumes tweets from producer
    '''
    # set-up a Kafka consumer
    consumer = KafkaConsumer('twitter_stream')

    for msg in consumer:
        data = json.loads(msg.value)
        text = data["text"]
        t = TextBlob(text)
        sentiment_polarity = t.sentiment.polarity
        if (sentiment_polarity > 0):
            result = "\"" + clean_tweet(text) + "\"" + ' - has positive sentiment'
            print(result)
        elif (sentiment_polarity == 0):
            result = "\"" + clean_tweet(text) + "\"" + ' - has neutral sentiment'
            print(result)
        else:
            result = "\"" + clean_tweet(text) + "\"" + ' - has negative sentiment'
            print(result)


main()