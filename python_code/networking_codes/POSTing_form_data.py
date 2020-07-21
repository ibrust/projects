
#demos making POSTs of form data. w/ urllib, encoding & constructing a request object (w/ a strange MIME type); w/ requests it's straightforward. 
#handling POSTs with urllib: 
from urllib.request import Request 
from urllib.parse import urlencode
from urllib.request import urlopen 
import json


data_dictionary = {'name': 'customer', 'phone': '3232322'} #The form data should be placed in a dictionary as key:value pairs
data = urlencode(data_dictionary).encode('utf-8') #the form data must then be encoded like query strings using urlencode.
req = Request('http://httpbin.org/post', data=data) #create a request object, pass the data & some headers to it
req.add_header('Content-Type', 'application/x-www-form-urlenode;charset=UTF-8') #Then you must add a Content-Type header and specify 
                                                                                #the specific MIME type: application/x-www-form-urlencoded
response = urlopen(req)                 #I believe the data must also be sent as bytes, but I'm not sure and don't see that taking place.
response_dictionary = json.load(response) 
print("URLLIB RESPONSE: ", response_dictionary, "\n________________________________________") 

#________________________________________________________
#handling POSTs with requests
#requests handles most of what must be done manually in urllib - headers, encoding 
#syntax: requests.post('URL', data = data_object, json = dictionary_object) --- not sure what the json does 

import requests 

response = requests.post('http://httpbin.org/post', data=data_dictionary) #requests automatically formats the dictionary, so you don't format it. 
try: 
    print("REQUESTS RESPONSE: ", response.text)
except: 
    pass 



