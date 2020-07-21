from urllib.request import urlopen 
import json 

response = urlopen('http://www.google.com') 
#you can do PUTs with your request by passing additional arguments to urlopen 

#response is an object of type http.client.HTTPResponse 
print(response, '\n\n__________________________________________\n') 

#the response has a variety of methods - read(), readline(), readlines(), close() 
print(response.readline(), '\n\n__________________________________________\n')

#you can also use the json library if the response is in json format - loading the response into a json object
response2 = urlopen('https://sampleserver6.arcgisonline.com/arcgis/rest/services/USA/MapServer?f=pjson')
json_response = json.loads(response2.read())
print(json_response, '\n\n__________________________________________\n')


#you can get the response status code from a response object - 200s are successes, 400s / 500s are errors, 300s are redirects, 100s are informational 
print(response2.status, '\n\n__________________________________________\n')


#urllib provides a way of handling errors: 
import urllib.error 
try: 
    urlopen('http://www.ietf.org/rfc/rfc0.txt') #I tried putting in a complete garbage URL and it threw another error for some reason 
except urllib.error.HTTPError as e: 
    print("Exception: ", e)
    print("Status: ", e.code) 
    print("reason: ", e.reason)
    print("URL: ", e.url,  '\n\n__________________________________________\n')


#you can retrieve the headers of the response in two ways:
if (response.code == 200): 
    print(response.headers) #returns a string of all the headers 
    #print(response.getheaders()) #returns a list of all the headers
print('\n__________________________________________\n') 


#the user-agent header is an important one, it identifies a client that uses HTTP. 
#in the following code, we create a request object then url_open by default adds the user-agent header to it, then we print that header: 
from urllib.request import Request 
request1 = Request('http://www.python.org') 
urlopen(request1)
print(request1.get_header('User-agent'), '\n__________________________________________\n')   #you'd use this to identify the client software that made the request


#you can add headers to requests before sending them - create a request object, add the header, then send w/ urlopen: 
#let's say a server interfaced with an Accept-Language header. You could do the following to change the response language: 
request2 = Request('http://www.debian.org') 
request2.add_header('Accept-Language', 'nl')    # nl is a 2 letter ISO language code for netherlands version of the language parameter, apparently... 
response3 = urlopen(request2) 
print(response3.readlines()[:5], '\n__________________________________________\n')

#you can retrieve the headers of a request also (different than a response): 
print(request2.header_items(), '\n__________________________________________\n')


#let's say you wanted to customize your user-agent header (which usually says the browser & OS you're running). You can do this in two ways: 
# you can use add_header like normally, or can pass a parameter of headers when you create the request: 
USER_AGENT = 'Mozilla/5.0 (Windows NT 5.1; rv:20.0) Gecko/20100101 Firefox/20.0' 
URL = 'http://www.debian.org' 
headers = {'Accept-Language': 'nl', 'User-agent': USER_AGENT}
request = Request(URL,headers=headers) 
for key, value in request.header_items(): 
    print(f'{key}:{value}')
#note that urlopen was not used - it might automatically wrap & overwrite these changes, but the author does not say specifically.
print('\n__________________________________________\n')


#Another important header, content-type, contains the MIME type & possibly the encoding - it's the main way HTTP indicates the kind of content being passed: 
print("content-type: ", response2.getheader('Content-Type'), '\n_______________________________________________\n') 


#Python has an HTML parser that allows you to parse the response: 
#There are obviously more details to getting this to work - it doesn't appear to work. It's supposed to extract links from a URL 
from html.parser import HTMLParser 
class custom_parser_link_extractor(HTMLParser): 
    def handle_start_tag(self, tag, attrs): 
        if (tag == "a"): 
            for a in attrs: 
                if (a[0] == 'href'): 
                    link = a[1] 
                    if (link.find('http') >= 0): 
                        print(link) 
                        new_parser = custom_parser_link_extractor() 
                        new_parser.feed(link)

url = "http://weevil.info/useful-website-links" 
request4 = urllib.request.urlopen(url) 
parser = custom_parser_link_extractor() 
parser.feed(request4.read().decode('utf-8'))
print("\n_____________________________________________________\n")


#this is another way to extract links from a URL, apparently - using regular expressions 
#This still works, apparently - not sure why the parser isn't working. 
import re 
def download_page(url): 
    return urlopen(url).read().decode('utf-8')
def extract_links(page): 
    link_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return link_regex.findall(page) 
target_url = 'http://weevil.info/useful-website-links' 
page1 = download_page(target_url) 
links = extract_links(page1) 
for link in links: 
    print(link) 
print("\n_____________________________________________________\n")


#******!!!!!!!!!!
#You can also use regular expressions to extract images from a page - just use it to find the img elements
# A very useful script: 
from urllib.request import urljoin 
def extract_image_locations(page): 
    img_regex = re.compile('<img[^>]+src=["\'](.*?)["\']', re.IGNORECASE) 
    return img_regex.findall(page) 
image_locations = extract_image_locations(page1) 
for src in image_locations: 
    print(urljoin(target_url, src))
print("\n_____________________________________________________\n")



#there's also a module for working with URLs: 
#the parsed_URL object has format: ParseResult(scheme='https', netloc='www.packtpub.com', path='/tech/Python', params='', query='', fragment='')
from urllib.parse import urlparse 
parsed_URL = urlparse('https://www.packtpub.com/tech/Python') 
print(parsed_URL)
#You can use urlparse to get the URLs query parameters: 
parsed_URL = urlparse('https://search.packtpub.com/?query=python')
print(parsed_URL.query)
#You can convert the queries to key/value pairs in a dictionary: 
from urllib.parse import parse_qs
print(parse_qs(parsed_URL.query))
#with the urlencode method, dictionaries of key/value pairs for queries can be easily encoded into URL strings also: 
from urllib.parse import urlencode 
query_string = urllib.parse.urlencode({"user": "user", "password": "ashwini2"})
print(query_string)
print("\n_____________________________________________________\n")


#you can also set up a proxy with urllib. you need a proxy IP & port number which you can find via searching google. 
#you then need to create a proxy handler and install an "opener" (like urlopen) for the proxy handler. 
import urllib.parse, urllib.request
proxy_pair = {"http" : "http://103.106.0.42:8080"} #protocol & URL 
URL = 'http://www.google.com'
proxy_handler = urllib.request.ProxyHandler(proxy_pair)
custom_opener = urllib.request.build_opener(proxy_handler) 
urllib.request.install_opener(custom_opener)
try: 
    response = urllib.request.urlopen(URL) 
    print("FROM PROXY: ", response.headers, '\n__________________________________________\n')
except: 
    print("PROXY is probably down, change proxies", '\n__________________________________________\n')
























