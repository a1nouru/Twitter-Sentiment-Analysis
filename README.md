# Twitter-Sentiment-Analysis
Analyzing reaction to tweets using TextBlob

* How Sentiment Analysis Works
1. Use twitter API to search for tweets with a specific mention
2. The search text is then broken down into chunks of words and sentences(Tokenization). 
3. After tokenization, textblob will calculate how often a tweet shows up based based on number of retweets and likes (Bag of Words model). From this, the measure of popularity can be determined.
4. Finally, the measure of reaction of a tweet is printed. 

* Makes sense right!

##  Setup 
  Install `Tweepy`
    
    git clone https://github.com/tweepy/tweepy.git
    
    cd tweepy
    
    python setup.py install
    
  Install `TextBlob`
  
    git clone https://github.com/sloria/TextBlob
    
    cd TextBlob
    
    python setup.py install 
    
## Create your twitter app **[here](https://developer.twitter.com/en/apps)**
![screen shot 2019-02-24 at 12 58 21 pm](https://user-images.githubusercontent.com/24802515/53305293-b8b78300-3834-11e9-9942-a7f10003f070.png)

##### And You're all set

![feb-24-2019 12-14-03](https://user-images.githubusercontent.com/24802515/53305327-38dde880-3835-11e9-9731-b37fd7cad644.gif)

