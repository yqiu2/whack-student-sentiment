import csv 
import sys
from TwitterSearch import *

#importing the databases of campuses & locations
campus_loc = {} #{name:[long:lat]}
with open('campuses.csv') as f:
    reader = csv.reader(f)
    reader.next()
    for row in reader:
        campus_loc[row[1]] = [float(row[3]), float(row[4])]

school = "Harvard University"
#school = raw_input("> ") - what you implement if you want to ask the user for a school name
print "We're going to look at %s." %school 

counter = 0 #this entire block will never be run unless we take user input
while school not in campus_loc.keys():
	counter += 1
	print "Sorry! Doesn't look like we have that school. Try again?"
	if counter > 5:
		print "Wow, you really suck at this."
	school = raw_input("> ")

location = campus_loc[school] #gets the location from campus_loc using the school name

############## begin Twitter API call now

try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords([' ']) # let's define all words we would like to have a look for
    tso.set_geocode(location[1],location[0],50)
    #tso.set_language('de') # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = 'naPGQJt3L75sZiEZAplsETEp1',
        consumer_secret = 'rqyRlly80nw1XUGxt7ySR2ZUvQiqDKpbj8kEgDXJ63U1AWbvAr',
        access_token = '16986893-Zq2L75kDTGR0l3AnsSN1ZXkzw4o8NuBssLCyvxkES',
        access_token_secret = 'woWPf0kgYoJcz6w4mNUBc8tt2bWqwdSCoMPEYXsWU9Y6w'
     )

     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)

