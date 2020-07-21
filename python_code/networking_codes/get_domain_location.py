#demos fetching an HTML document from  a site that provides additional functionality
#then simply manually parsing the response and using the results
from lxml.html import fromstring 
import requests

domain = input("Enter the domain (i.e. http://www.packtpub.com): ") 
url = 'http://whois.domaintools.com/' + domain 
headers = {'User-Agent': 'wswp'} 
response = requests.get(url, headers=headers)

html_text = response.text 
parsed_html_tree = fromstring(html_text)                    # got the HTML text and turned it into a parsed tree

info = parsed_html_tree.xpath('//*[@id="stats"]//table/tbody/tr//text()')   # query for particular elements within the tree - what's the return type of xpath?
temp_list = [] 

for each in info:                                       #loop through each identified element and format / place into a list
    each = each.strip() 
    if each == "": 
        continue 
    temp_list.append(each.strip("\n")) 

ip_index = temp_list.index("IP Address")                #use the obtained information as necessary
print("IP address ", temp_list[ip_index + 1])
location1 = temp_list.index("IP Location") 
location2 = temp_list.index("ASN") 
print("Location : ", "".join(temp_list[location1 + 1:location2]))

