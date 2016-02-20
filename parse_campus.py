import indicoio

# need to import twitter API
# api key for indicoio and twitter
import csv 
import sys


campus_loc = {} #{name:[long:lat]}
with open('campuses.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        campus_loc[row[1]] = [float(row[3]), float(row[4])]

print campus_loc

'''
campuses = {}
for c in campuses:
    if len(campuses[c]) > 200:
'''
