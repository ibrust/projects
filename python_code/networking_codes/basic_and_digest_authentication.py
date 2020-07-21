#Basic authentication & Digest authentiation are the two authentication models supported by HTTP protocol
#Basic uses base64 encoding on 'user: password'. (?) 
#Digest uses MD5 sum encryption on hashes - user, key, and realm hashes. this is the secure method, basic does not encrypt it only encodes 
#Both of these are described in 'Learning Network Python' on page 79-80, and I will only show how requests implements them: 

#Basic Authentication: 
import requests 
from requests.auth import HTTPBasicAuth, HTTPDigestAuth 

response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('ibrust', 'Ashwini2'))
print(response.status_code) 
response2 = requests.get('https://api.github.com/user', auth=HTTPDigestAuth('ibrust', 'Ashwini2'))
print(response2.status_code)

