import csv 
import sys
import string
import indicoio
from TwitterSearch import *
from indicoio import political, sentiment, language, text_tags, keywords, fer, facial_features, image_features
from openpyxl import Workbook

def remove_http(source_string, replace_what): #defining a funciton for pulling out the links in the tweets, that rhymes haha
    head, sep, tail = source_string.rpartition(replace_what)
    return head 

def convert(schoolName):
    #importing the databases of campuses & locations

    campus_loc = {} #{name:[long:lat]}
    with open('campuses.csv') as f:
        reader = csv.reader(f)
        reader.next()
        for row in reader:
            campus_loc[row[1]] = [float(row[3]), float(row[4])]

    school = schoolName #takes input and renames it for convenience's sake since every other variable name is schoolName #whoops

    """
    counter = 0 #this entire block will never be run unless we take user input
    while school not in campus_loc.keys():
            counter += 1
            print "Sorry! Doesn't look like we have that school. Try again?"
            if counter > 5:
                    print "Wow, you really suck at this."
            school = raw_input("> ")
    """
    location = campus_loc[school] #gets the location from campus_loc using the school name

    ############## begin Twitter API call now

    try:
        tso = TwitterSearchOrder() # create a TwitterSearchOrder object
        tso.set_keywords([' ']) # let's define all words we would like to have a look for
        tso.set_geocode(location[1],location[0],1)
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
        collegeTweets = []
        counter = 0
        for tweet in ts.search_tweets_iterable(tso):
            if counter < 321:
                collegeTweets.append(tweet['text'].encode('ascii','ignore')) #ignores any ASCII
                collegeTweets[-1] = string.replace(collegeTweets[-1],"#","") #pulls out pound signs to make hashtags part of the sentence/string
                collegeTweets[-1] = string.replace(collegeTweets[-1],"\n","")  #pulls out any returns which fuck up the sentence
                collegeTweets[-1] = string.replace(collegeTweets[-1],"@","") #pulls out any mentions
                collegeTweets[-1] = remove_http(collegeTweets[-1],"http") #pulls out any links (aka to pictures since the majority of these are linked from Instagram)
                counter += 1
                collegeTweets[-1] += "a"
                print collegeTweets[-1]

    except TwitterSearchException as e:
        print(e)    

    ############### begin Indico API call now

    indicoio.config.api_key = "f09f509655f721e3adac6df5b35abfed"
    api_key_Lisa = "f09f509655f721e3adac6df5b35abfed"

    sentementCollegeTweets = sentiment(collegeTweets) #take the Twitter string agnd put it into our own string because we needed an array of the indico results

    average = 0.0
    for i in sentementCollegeTweets:
        average += i
    average = average/len(sentementCollegeTweets)

    print average
    return average


#creating the Workbook for the locations & naming the first tab 
wb = Workbook()
ws = wb.active
            """      
            school1 = convert("Pepperdine University")
            ws['A1'] = school1
            """
for openpyxl.worksheet.campus1.columns():
    

wb.save("sample.xlsx")
