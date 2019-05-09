import csv
import re
import pandas as pd
import numpy as np
from textblob import TextBlob
from googletrans import Translator
import preprocessor as p

infile = 'congresstweets.csv'
def clean_tweet(tweet): 
        ''' 
        Utility function to clean tweet text by removing links, special characters 
        using simple regex statements. 
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

c = 0

with open('outcongress.csv','w') as writeFile:
	with open(infile, 'r') as readfile:
	    rows = csv.reader(readfile)
	    writer = csv.writer(writeFile)
	    writer.writerow(['Date', 'Tweets', 'Location', 'Sentiment Polarity'])
		
	    for row in rows:
			sentence = row[1]
			sentence = clean_tweet(sentence)
			sentence = Translator().translate(sentence)

			c=c+1
			'''
			if c%20 == 0:
				 time.sleep(20) # Delay for 1 minute (60 seconds).
			'''
			blob = TextBlob(sentence)
			print (sentence)
			print (blob.sentiment.polarity)
			
			date = str(row[0])
			twe = str(sentence)
			loc = str(row[2])
			pol = float(blob.sentiment.polarity)		
			writer.writerow([date, twe, loc, pol])
		
