import pyshark 
packets_array = [] 

def counter(*args): 
    packets_array.append(args[0]) 

def count_packets(): 
    cap = pyshark.FileCapture('./packets_for_pyshark2.cap', only_summaries=True) 
    cap.apply_on_packets(counter, timeout=10000)       #apply_on_packets uses a callback, the argument to counter will be individual packet
    return len(packets_array) 

print("Total packets: ", str(count_packets()))

#takes some time - only_summaries helps speed it up, perhaps you could rewrite this in C with pthreads for very large files 