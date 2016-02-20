#WHACK 2016

import indicoio
from indicoio import political, sentiment, language, text_tags, keywords, fer, facial_features, image_features

indicoio.config.api_key = "f09f509655f721e3adac6df5b35abfed"
api_key_Lisa = "f09f509655f721e3adac6df5b35abfed"

result1 = political("Guns don't kill people. People kill people.")
result2 = sentiment("It's so cold outside!")
result3 = sentiment("I'm doing okay")
result4 = sentiment("indico is so easy to use!")
result5 = sentiment("this api isn't bad at recognizing double negatives either.")

result6 = sentiment("I'm doing okay")
result7 = sentiment("Best day ever!")

#print result1
print result7
