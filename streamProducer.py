
import tweepy
from kafka import KafkaProducer
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener


consumer_key = "I5tJA3eJcG9yjY87YK6b04nCM"
consumer_secret = "30HerPjWxRw6mnBkTcchqJ8i19GTHulTWkGVr5vO8paOP5Erjw"
access_token = "1062964050202673153-pGGgbivQLg68SR3Okx50rah70HJuz7"
access_secret = "NYlsPp2vDMY5P9uHVfJ0YHaam8IqzJS4yON7x59mXBIw4"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

class KafkaPushListener(StreamListener):
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'])


    def on_data(self, data):

        self.producer.send("twitter_stream", data.encode('utf-8'))
        print(data)
        return True

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, KafkaPushListener())

twitter_stream.filter(track=['#trump'])
