# Twitter-Sentiment-Analytics
Basic Twitter Sentiment Analytics using Apache Spark Streaming APIs and Python by processing live tweets from Twitter.

### Objectives:
* Perform Sentiment Analysis over live-streaming tweets from Twitter using Twitter API and Apache Spark. 
* Using Apache Kafka to buffer live tweets data fetched with help of Twitter API.
* Using stream processing API provided by Spark convert the live data to DStreams and classify each as positive and negative.
* Plot the variation of word counts with respect to time period using python's MatPlotLib.
* Data-set for positive and negative words were static text files each consisting 3000+ words.

### Steps:
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
### Sample Date
```
TONIGHT IS A NIGHTMARE
Who needs therapy after this episode #TheWalkingDead 

🙋🏻🙋🏼🙋🏽🙋🙋🏾🙋🏻🙋🏼🙋🏾🙋🏽🙋🏻🙋🏼🙋🏾🙋🏽🙋🏻🙋🏼🙋🏾🙋🏽🙋🏻🙋🏼🙋🏾🙋🏽🙋🏻🙋🏼🙋🏾🙋🏽🙋🏻🙋🏼🙋🏾🙋🏽🙋🏻🙋🏼🙋🏾🙋🏽
I bet we know who everyone will be for #Halloween #Negan #Lucille #TheWalkingDead https://t.co/p4lBeuLSxZ
Okay but honestly... Jim would vote for Trump, right?
No matter how many times we fight you're my bestfriend and no matter what I will stop and listen to you. Dont forget that.
The tables will turn. #TheWalkingDead
@SydneyKoolstra and I have decided to involve our selves in what @10_shelby_10 is for Halloween. Choose wisely.
@ABC how does one actually offend a pornstar, that's not possible
Yeah fuck you negan #TheWalkingDead
I liked him tooo BUT BRUHHH
How's my little skunk butt already 2 months old😭😭😭 Auntie mo needs you to stop growing up so quick😭🐒💕 https://t.co/IIesieiS6B
Imma have to smoke now instead of am cause im in bad mood
That axe is gona play a huge role this season #TheWalkingDead
#TheWalkingDead thought this show was about zombies 😭😭😭😭😭 wtf
🌹👁🌹🙏🏾BLESSED EVENING EVERYONE BE SAFE AND ENJOY FOLLOW THE CHOO CHOO🚂💨🌹👁🌹💯@TAMMYYO86840808 @_Mr_Clutch_3… https://t.co/IcIfU3Agqw
Finally watching Hocus Pocus ☺️🎃🎃
@jayhamilton87 would've been quite the player
How they had us wondering if Glenn was dead or alive and then still kill him? smh  #TheWalkingDead
@TylerSimi 😂😂😂 lol you're the best. thank you silly
Thanks to Prague, I now have my 10th tattoo. Also thanks to Prague, it's 3 am and I am doing homework.
@kevinmelrose94 thank you Aaron!
Robbery | Maple Leaf Dr &amp; Jane St Black Cr S Ramp [12 Div.] 10/23 21:53 #Toronto_Division
What about classy ? I only het hood when needed too 😂 https://t.co/1rLHASZBN1
you're the sweetest. 😭❤️ miss you! https://t.co/frnFvXaYnd
Thanks Cubs! #cubswin #eiuhomecoming2016 @ Eastern Illinois University https://t.co/NQbOxZaWTG
I drop off chase then we immediately get on FaceTime..
After so many years of #TheWalkingDead I just don't think I can watch this show anymore.
@HBfromKC I'm so sorry. I'll behave.
OMG! I honestly don't even know my current emotional state right now... #TheWalkingDead
If you know you couldn't do anything tonight, why wouldn't you say that from the jump?? 🙄
```
### Sentiment Plot:

Plot between positive and negative words in a time frame:

![alt text](https://github.com/sudhansusingh22/Twitter-Sentiment-Analytics/blob/master/plot.png "Sentiment Plot")




