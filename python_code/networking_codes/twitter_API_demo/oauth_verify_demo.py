import requests, requests_oauthlib, sys 

def init_auth(file):
    (CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET) = open(file, 'r').read().splitlines() #get the various keys from access_keys.txt
    auth_obj = requests_oauthlib.OAuth1(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET) #returns an authorization object that requests.get accepts
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

if __name__ == '__main__': 
    auth_obj = init_auth('access_keys.txt')  