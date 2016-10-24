# Twitter-Sentiment-Analytics
Basic Twitter Sentiment Analytics using Apache Spark Streaming APIs and Python by processing live tweets from Twitter,

* Perform Sentiment Analysis over live-streaming tweets from Twitter using Twitter API and Apache Spark. 
* Using Apache Kafka to buffer live tweets data fetched with help of Twitter API.
* Using stream processing API provided by Spark convert the live data to DStreams and classify each as positive and negative.
* Plot the variation of word counts with respect to time period using python's MatPlotLib.
* Data-set for positive and negative words were static text files each consisting 3000+ words.

```
1. #Start zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties

      #stop zookeeper
      sudo service zookeeper stop

2. #start kafka server
bin/kafka-server-start.sh config/server.properties

3. # create a topic
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic twitterstream

4. # list all topics
bin/kafka-topics.sh --list --zookeeper localhost:2181

5. # Provide twitter credentials without quote in twitter.txt

6. #start streaming twitter data
python twitter_to_kafka.py

7. #check streamed data
bin/kafka-console-consumer.sh --zookeeper localhost:2181 --topic twitterstream --from-beginning

8. #do sentiment analysis on data
$SPARK_HOME/bin/spark-submit --packages org.apache.spark:spark-streaming-kafka_2.10:1.5.1 twitterStream.py
```
