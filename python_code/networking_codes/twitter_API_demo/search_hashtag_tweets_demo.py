#this uses the twitter API, while search_tweets and get_mentions are just requests to an endpoint
import twitter 

def twitter_connection(path_file): 
    with open(path_file, 'r') as file: 
        (CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET) = file.read().splitlines() 
        auth = twitter.oauth.OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET) #note this oauth function is provided by twitter module
        return twitter.Twitter(auth=auth)

def get_info_twitter(tw): 
    if tw is not None: 
        query = tw.search.tweets(q="#python", lang="en", count="20")["statuses"] #the twitter API transmits data in json, but the twitter module translates
        for q in query:                                                          #the data into a python dictionary as needed. however, you can still work
            for key, value in q.items():                                         #with the json, i.e. dump it to file: json.dumps(query, file_obj, indent=1)
                if (key == 'text'): 
                    print(value + '\n') 

def main(): 
    try: 
        tw = twitter_connection("access_keys.txt") 
        get_info_twitter(tw) 
    except Exception as e: 
        print(str(e)) 

if __name__ == "__main__": 
    main() 