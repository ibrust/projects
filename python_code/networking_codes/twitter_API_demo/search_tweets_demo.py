#no twitter API, but just requests to an endpoint 
import requests, requests_oauthlib, sys, json 

def init_auth(file):
    (CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET) = open(file, 'r').read().splitlines() #get the various keys from access_keys.txt
    auth_obj = requests_oauthlib.OAuth1(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET) #returns an authorization object that requests.get accepts.
    if verify_credentials(auth_obj):
        print('Validated credentials successfully!')
        return auth_obj 
    else: 
        print('Credential validation failed') 
        sys.exit(1)

def verify_credentials(auth_obj):
    url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
    response = requests.get(url, auth=auth_obj)                        #requests accepts the authorization object generated w/ requests_oauthlib
    return response.status_code == 200 

def search(auth_obj):               #makes a request to a twitter REST endpoint - not the same as using the twitter API, apparently 
    params = {'q': 'python'}                                       #search term will be python 
    url = 'https://api.twitter.com/1.1/search/tweets.json'         #the rest endpoint for searching tweets 
    response = requests.get(url, params=params, auth=auth_obj)     
    return response 

if __name__ == '__main__': 
    auth_obj = init_auth('access_keys.txt') 
    response = search(auth_obj) 
    print(json.dumps(response.json(), indent=2))        #this line formats the output as an indented json string 

