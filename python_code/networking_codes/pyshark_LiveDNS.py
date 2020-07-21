#monitor WIFI and print packets with "DNS" in the packet
import pyshark 

capture = pyshark.LiveCapture(interface="Wi-Fi")

for packet in capture: 
    if "DNS" in packet and not packet.dns.flags_response.int_value: 
        print(packet.dns.qry_name)