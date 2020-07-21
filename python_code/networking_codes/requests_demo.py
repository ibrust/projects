#basic demo of making a request & printing information. 
import requests
response = requests.get('http://www.github.com') 
print(response) 
print(response.status_code)
print("\n__________________________________")
print(response.content) 
print("\n__________________________________")
print(response.reason) 
print("\n__________________________________")
print(response.url)
print("\n__________________________________")

print("HTTP response in raw text form: ", response.text)
print("\n__________________________________")


#response.headers is a dictionary. this will only loop over the keys: 
for header in response.headers:
    print(header)
print("\n__________________________________")
#but you also might want to iterate over the key / values: 
for key, value in response.headers.items(): 
    print("%s: %s" % (key, value))
print("\n__________________________________")


print("CONTENT TYPE: ", response.headers['content-type'])
print("\n__________________________________")
#requests automatically sets accept-encoding to gzip and deflate, which makes the message zipped by default somehow. 
print("ACCEPT-ENCODING: ", response.headers['content-encoding']) #key is different than accept-encoding in the dictionary for some reason? 
print("\n__________________________________")

#requests is able to make json requests, receive json & specify the structure of the json received (as key value pairs here...?):
response3 = requests.post("https://sampleserver6.arcgisonline.com/arcgis/rest/services/USA/MapServer?f=pjson", json={"key": "value"})
print("JSON RESPONSE: ", response3.json(), "\n__________________________________")





#You can make proxy requests as well: 
proxy_URL = "http://104.255.169.45:5836" 
proxy_pair = {"http": proxy_URL}
try: 
    response2 = requests.get("http://www.google.com", proxies=proxy_pair)
    print("PROXY RESPONSE: ", response2.url)
except: 
    print("PROXY OFFLINE PROBABLY")
print("\n__________________________________")

#pip install requests-oauthlib <-- a library you can install for working with OATH APIs. Many large tech companies APIs use Oauth





