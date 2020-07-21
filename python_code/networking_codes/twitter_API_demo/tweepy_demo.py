#gets tweets in real time matching a keyword - uses a streaming API inherited from tweepy 
import tweepy
import json 

def twitter_connection(path_file): 
    with open(path_file, 'r') as file: 
        (CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET) = file.read().splitlines() 
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)           #tweepy's way of performing OAuth authentication
        auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
        return (tweepy.API(auth), auth)

#class that listens to the flow of tweets - inherits from tweepy, code is fairly cryptic 
class StreamListener(tweepy.StreamListener): 
    def on_data(self, data): #when a tweet matches the searched for terms, it is passed to this function, which prints the text content 
        data = json.loads(data) 
        print(data['text']) 
        return True 
    
    def on_limit(self, track):  #there's a limit of calls, apparently, and this function is called when that limit is reached 
        print('[!] Limit: {0}').format(track)
        sleep(10) 

    def on_error(self, status): #interrupts the listener in case of an error 
        print('[!] Error: {0}').format(status) 
        return False 

def streamAPI(auth): 
    listener = StreamListener()                             #instantiate custom listener
    streamer = tweepy.Stream(auth=auth, listener=listener)  #start the stream 
    targetTerms = ['python']                                #terms passed to the stream 
    streamer.filter(track=targetTerms)                      #filter for those terms 

def getTrendingTopics(woeid=1):                     #gets the currently trending topics. not used in this program but could be used if desired 
    trends = api.trends_place(1)[0]['trends']               #woeid was never used either, not sure what it was for... author put it there 
    trendList = [trend['name'] for trend in trends] 
    return trendList 

def main(): 
    try: 
        tweepy_API, auth = twitter_connection("access_keys.txt") #tweepy_API was returned but never used - presumably it could be used
        streamAPI(auth) 
    except KeyboardInterrupt: 
        exit(1) 

if __name__ == "__main__": 
    main()