# Twitter Sentiment Analysis

A simple application to analyze the sentiment of tweets.
Basic structure involves storing the tweets in kafka topic say “Twitter_stream” and then using spark streaming processing those tweets and finally consuming the final sentiment result.
For sentiment calculation – used TextBlob
To run the application
-	Run zookeeper (bin\zookeeper-server-start.sh config\zookeeper.properties)
-	Run Kafka (bin\kafka-server-start.sh config\server.properties)
-	Run the streamProducer.py
-	Run the streamConsumer.py
