#python lists or dictionaries can be converted to strings, and strings can be converted into python lists or dictionaries: 
import json
var_1 = ['three', 'four']
python_object = {'A':False, 'B':['one', 'two'], 'C':'option_C', 'D':var_1} 
json_string = json.dumps(python_object); 
print("JSON STRING: ", json_string, "\n__________________________") 
python_object = json.loads(json_string) 
print("RECONVERTED PYTHON LIST: ", python_object, "\n__________________________")

#you can also convert a json file into a python list or dictionary: 
with open("json_string.json", "r") as json_file:
    python_object = json.loads(json_file.read())        #read() from the file gets a string which is then converted
    print("CONVERTED FROM FILE: ", python_object, "\n__________________________")


