import tweepy
import urllib

consumer_key=''
consumer_secret=''
access_token=''
access_token_secret=''

dir = './images/'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    try:
        j = 0
        for i in tweet.extended_entities['media']:
            print(i['media_url'])
            img = urllib.request.urlopen(i['media_url'])
            localfile = open(dir + str(tweet.id) + str(j), 'wb')
            localfile.write(img.read())
            img.close()
            localfile.close()
            j = j+1
    except:
        print('No Image')

#searched = api.saved_searches()
#for data in 
