
#URLLIB cookie handling: 
#this automatically extracts cookies from a received request and stores them in the cookie jar ...
import urllib 
from http.cookiejar import CookieJar 

cookie_jar = CookieJar() 
cookie_processor = urllib.request.HTTPCookieProcessor(cookie_jar)   #tell the cookie processor which jar to store its cookies in 
custom_opener = urllib.request.build_opener(cookie_processor)   #build a custom opener so that we can open a URL with these cookies working
urllib.request.install_opener(custom_opener)
custom_opener.open('http://www.github.com')     # you use the custom opener instead of urlopen apparently 
print("TOTAL COOKIES: ", len(cookie_jar), "\n_______________________________")   #we can now see our cookie jar is filled with some cookies 
                                            #that will be remembered on future requests with this opener

cookies = list(cookie_jar) 
for one_cookie in cookies: 
    print(one_cookie, "\n_______________________________")
print("_________________________________")
#Cookies have some interesting attributes: expires, HttpOnly, secure 
#expires tells the cookies remaining lifespan
#HttpOnly is a flag that only allows the client to access the cookie during HTTP requests - this prevents cross-site scripting attacks. 
#secure is a flag that indicates https should be used to send the cookie 

#__________________________________________________________________________________
#__________________________________________________________________________________
#REQUESTS cookie handling: 
import requests 
#One way to access the cookies is just through an attribute of the response, 
#which should contain a requests.cookies.RequestsCookieJar object with a list of the cookies: 
response = requests.get('http://www.github.com') 
print("REQUESTS COOKIE RESPONSE: ", response.cookies, "\n_______________________________") 

#Another way is using requests.Session and observing the cookies from the request & response: 
session = requests.Session() 
print(session.cookies.get_dict()) 
response = session.get('http://github.com') 
print(session.cookies.get_dict(), "\n_______________________________")

#lastly, you can use requests.get, which has a cookies parameter, to send cookies to the server: 
cookies = [] 
url = "http://httpbin.org/cookies" 
cookies = dict(admin='True')    #this is what the cookie contains, apparently - some unknown specifier 
cookies_response = requests.get(url, cookies=cookies)     #the cookie parameter will pass those cookies with the request 
print("response to request sent with cookies: ", cookies_response.text) #did it send your own cookie back as the response...? 
