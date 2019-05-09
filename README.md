# Twiiter Tweets analysis using Spatial Algorithms


This project investigates how to organize and classifya large collection of real time Twitter data, working with a dataset  of  almost  3  Lakhs  tweets  collected  directly  from  Twitter.The  approach  described  here  combines  spatial  analysis  of  thelocation  of  the  tweet  with  content/sentiment  analysis  of  the  textand  hash-tags  associated  with  the  same  tweet.  We  then  lookinto  those  specific  regions  to  try  and  identify  the  most  popular Political  Party  and  its  influence  on  the  regions  and  comparedifferences  between  each  city,  to  provide  a  better  plan  for  the Political  Party  Campaign.  We expect  our  results  to  vary  basedon  where  people  are  tweeting  from  and  which  Political  Partyhas  more  impact  in  the  city.

### Tech

We used a number of libraries and API.

* Python
* Tweepy API to fetch Tweets
* googletrans to convert HINGLISH word to ENGLISH word
* csv to handle csv file and data
* Textblob to find the senitment of the tweets


### Installation

Install Tweepy

```sh
$ pip install tweepy
```

Install googletrans
```sh
$ pip install googletrans
```
Install textblob
```sh
$ pip install -U textblob
$ python -m textblob.download_corpora
```



### Development
After directing to the project folder run the python file.
Collect the tweets from Twitter
```sh
$ python tweets_final.py
```
Clean the tweets, convert Hinglish tweets to English, and find sentiment of each tweet.
```sh
$ python sentiment.py
```
CLuster tweets on the basis of different location in the previous dataset and count total number of positive, negative and neutral sentiments of that location.
```sh
$ python counting.py
```
Plot the countbjpcity.csv and countcongresscity.csv using Qgis and its library MMQGIS and OpenLayerMap.

