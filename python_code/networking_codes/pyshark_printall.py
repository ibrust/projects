import pyshark 
capture = pyshark.FileCapture('./packets_for_pyshark.pcap')

#the pcap file is 16kb, so it's quite large 
for pack in capture: 
    print(pack)


#the syntax print(capture[0]) only works in the interpreter and not in code, apparently - who knows why 
#print(capture[0])