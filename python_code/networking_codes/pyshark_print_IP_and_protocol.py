import pyshark 

capture = pyshark.FileCapture('./packets_for_pyshark.pcap', keep_packets=False)

def print_info_layer(packet): 
    try:
        print("Protocol: ", packet.highest_layer, "\t\tSource IP: ", packet.ip.src, "\tDestination IP: ",  packet.ip.dst) 
    except: 
        print("Packet is missing a protocol or IP attribute ")

#apply_on_packets takes a callback which will be applied to every packet 
capture.apply_on_packets(print_info_layer) 
