
import tweepy
from kafka import KafkaProducer
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener


consumer_key = "*************"
consumer_secret = "***********"
access_token = "**************"
access_secret = "***********"

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
