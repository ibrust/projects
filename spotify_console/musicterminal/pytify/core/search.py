import requests 
import json 
import urllib.parse


from .search_type import SearchType 
from pytify.core import read_config 


def _search(criteria, auth, search_type): 

    conf = read_config() 

    if not criteria: 
        raise AttributeError('Parameter `criteria` is required') 

    q_type = search_type.name.lower()
    url = conf.base_url + "/search?q=" + urllib.parse.quote_plus(f'{criteria}') + "&type=" + urllib.parse.quote_plus(f'{q_type}')

    print("SEARCH IS: ", url)

    headers = {'Authorization': f'Bearer {auth.access_token}'} 
    response = requests.get(url, headers=headers) 

    return json.loads(response.text) 


def search_artist(criteria, auth): 
    return _search(criteria, auth, SearchType.ARTIST) 

def search_album(criteria, auth): 
    return _search(criteria, auth, SearchType.ALBUM) 

def search_playlist(criteria, auth): 
    return _search(criteria, auth, SearchType.PLAYLIST) 

def search_track(criteria, auth): 
    return _search(criteria, auth, SearchType.TRACK) 


