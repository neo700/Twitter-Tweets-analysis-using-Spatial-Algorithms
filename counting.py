import csv
import re
import pandas as pd
import numpy as np
from collections import defaultdict, Counter
lis = defaultdict(list)
with open('countcongress.csv', 'r') as readfile:
	rows = csv.reader(readfile)
		
	for row in rows:
		lis[row[2]].append(row[3])		

with open('countcongresscity.csv','w') as writeFile:
	
	writer = csv.writer(writeFile)
	writer.writerow(['Location', 'Positive', 'Negative', 'Neutral', 'Total'])
	for k, v in lis.items():
		lt = 0
		gt = 0
		eq = 0	
		for i in range(len(v)):
	    		if float(v[i]) < 0:
				lt = lt + 1
			elif float(v[i]) > 0:
				gt = gt + 1
			else:
				eq = eq + 1

		writer.writerow([k, gt, lt, eq, len(v)])

