import tweepy
import csv
import pandas as pd

access_token = "XXXX"
access_token_secret = "XXXX"
consumer_key = "XXXX"
consumer_secret = "XXXX"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

bjp = 'bjptweets.csv'
congress = 'congresstweets.csv'

bjp_keywords = '#BJP OR #bjp OR BJP OR Modi OR modi OR abkibaarmodisarkar OR maibhichowkidar'
congress_keywords = '#congress OR #CONGRESS OR RahulGandhi OR rahul OR priyankagandhi'

csvFile = open(bjp, 'a')
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q=bjp_keywords,geocode="21.146633,79.088860,1756km",count=100,lang="en").items():
    print (tweet.created_at, tweet.text, tweet.user.location, tweet.user.followers_count)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.user.location.encode('utf-8'), tweet.user.followers_count])
