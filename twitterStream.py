from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import operator
import numpy as np
import matplotlib.pyplot as plt


# Declaring conf and sc as global variable to use in other functions
conf = SparkConf().setMaster("local[2]").setAppName("Streamer")
sc = SparkContext(conf=conf)

def main():
   # conf = SparkConf().setMaster("local[2]").setAppName("Streamer")
    #sc = SparkContext(conf=conf)
    ssc = StreamingContext(sc, 10)   # Create a streaming context with batch interval of 10 sec
    ssc.checkpoint("checkpoint")

    pwords = load_wordlist("positive.txt")
    nwords = load_wordlist("negative.txt")
   
    counts = stream(ssc, pwords, nwords, 100)
    make_plot(counts)


def make_plot(counts):
    """
    Plot the counts for the positive and negative words for each timestep.
    Use plt.show() so that the plot will popup.
    """

    for count in counts:
        if len(count) ==1:
            if count[0][0] == "positive":
                count.append(("negative",0))
            else:
                count.insert(0,("positive",0))
        elif len(count) ==0:
            count.insert(0,("positive",0))
            count.append(("negative",0))       
     
    #print counts                  
    positive = []
    negative = []

    for count in counts:
        positive.append(count[0][1])
        negative.append(count[1][1])

    maximum = max(max(positive),max(negative)) + 75
    xlen = len(positive)+1
    plt.plot(positive, color = "b", marker="o", markerfacecolor="b")
    plt.plot(negative, color = "g", marker="o", markerfacecolor="g")
    plt.xticks(np.arange(-1, len(positive)+1, 1))
    xticks = plt.gca().xaxis.get_major_ticks()
    xticks[0].set_visible(False)
    plt.yticks(np.arange(0, maximum, 25))
    plt.xlabel('Time step')
    plt.ylabel('Word count')
    plt.legend(['positive', 'negative'], loc='upper left')
    plt.savefig("plot.png")
    plt.show()
        
    # YOUR CODE HERE



def load_wordlist(filename):
    """ 
    This function should return a list or set of words from the given filename.
    """
    #conf = SparkConf().setMaster("local[2]").setAppName("Streamer")
    #sc = SparkContext(conf=conf)
    rdd = sc.textFile(filename)
    return set(rdd.collect())
    # YOUR CODE HERE



def fx(word,pwords,nwords):
    if word in pwords:
        return "positive"
    elif word in nwords:
        return "negative"
    else:
        return None

def updateFunction(newValues, runningCount):
    if runningCount is None:
       runningCount = 0
    return sum(newValues, runningCount) 

def stream(ssc, pwords, nwords, duration):
    kstream = KafkaUtils.createDirectStream(
        ssc, topics = ['twitterstream'], kafkaParams = {"metadata.broker.list": 'localhost:9092'})
    tweets = kstream.map(lambda x: x[1].encode("ascii","ignore"))
    words = tweets.flatMap(lambda line: line.split(" "))
    pairs = words.map(lambda word: (fx(word,pwords,nwords), 1)).filter(lambda x: x[0]=="positive" or x[0] == "negative")

    wordCounts = pairs.reduceByKey(lambda x, y: x + y)
    #wordCounts = wordCounts.filter(lambda x: x[0]=="positive" or x[0] == "negative")

    running_counts = pairs.updateStateByKey(updateFunction)

    running_counts.pprint()

# Print the first ten elements of each RDD generated in this DStream to the console

    # Each element of tweets will be the text of a tweet.
    # You need to find the count of all the positive and negative words in these tweets.
    # Keep track of a running total counts and print this at every time step (use the pprint function).
    # YOUR CODE HERE
    
    
    # Let the counts variable hold the word counts for all time steps
    # You will need to use the foreachRDD function.
    # For our implementation, counts looked like:
    #   [[("positive", 100), ("negative", 50)], [("positive", 80), ("negative", 60)], ...]
    counts = []
    wordCounts.foreachRDD(lambda t,rdd: counts.append(rdd.collect()))
    ssc.start()                         # Start the computation
    ssc.awaitTerminationOrTimeout(duration)
    ssc.stop(stopGraceFully=True)

    return counts


if __name__=="__main__":
    main()
