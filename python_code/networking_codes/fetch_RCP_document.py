#demos a simple get request and some command line input 
import urllib.request, sys, requests, socket 

try: 
    rfc_number = int(sys.argv[1]) 
except (IndexError, ValueError):
    print("supply RFC number as command line argument") 
    sys.exit(2) 
url = f'http://www.rfc-editor.org/rfc/rfc{rfc_number}.txt'

#DEMO of requests - simpler than urllib.request or sockets:
rfc_raw = requests.get(url).text 
print(rfc_raw) 


#DEMO of urllib.request: 
#rfc_raw = urllib.request.urlopen(url).read() 
#print(rfc_raw.decode())



#DEMO of sockets author provided which does not even work, doesnt return the full RFC, but only a header or something like that: 
#host = 'www.rfc-editor.org' 
#port = 80 
#sock = socket.create_connection((host, port)) 

#req = (f'GET /rfc/rfc{rfc_number}.txt HTTP/1.1\r\n'
#       f'Host: {host}:{port}\r\n'
#       f'User-Agent: Python {sys.version_info[0]}\r\n'
#       'Connection: close\r\n'
#       '\r\n')

#sock.sendall(req.encode('ascii'))

#rfc_bytes = bytearray() 
#while (True): 
#    buf = sock.recv(4096) 
#    if not len(buf): 
#        break 
#    rfc_bytes += buf 
#rfc = rfc_bytes.decode('utf-8')
#print(rfc) 


