import xml.etree.ElementTree as ElementTree             

#create and manipulate a structure of XML nodes 
root = ElementTree.Element('root')      #creates a new XML element named root
ElementTree.dump(root)                  #ElementTree.dump prints the XML passed to it - and returns None

book = ElementTree.Element('book') 
root.append(book)                       #XML nodes can append child nodes 
ElementTree.dump(root) 

name = ElementTree.SubElement(book, 'name')          #spawns a child node off of a parent element
name.text = "Learning Python Networking" 
ElementTree.dump(root) 

temp = ElementTree.SubElement(root, 'temp') 
ElementTree.dump(root) 
root.remove(temp)                           #XML nodes can remove child nodes 
ElementTree.dump(root) 

print("\n_________________________________")
import xml.dom.minidom as minidom 
print(minidom.parseString(ElementTree.tostring(root)).toprettyxml())   #prints a formatted XML DOM, not sure which parts minidom vs. toprettyxml do




