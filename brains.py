import csv 
import sys

#importing the databases of campuses & locations
campus_loc = {} #{name:[long:lat]}
with open('campuses.csv') as f:
    reader = csv.reader(f)
    reader.next()
    for row in reader:
        campus_loc[row[1]] = [float(row[3]), float(row[4])]

school = "Pepperdine University"
print "We're going to look at %s." %school 

if school not in campus_loc.keys():
	print "Sorry! Doesn't look like we have that school. Try again?"
	school = raw_input("> ")
else:
	#callTwitter


#drop listTweets into the indico.io API, get back an int between 0 & 1, call it sentiment

if sentiment 

