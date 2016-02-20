from TwitterSearch import *
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['the']) # let's define all words we would like to have a look for
    tso.set_geocode(52.5233,13.4127,50)
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
