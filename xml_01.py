##import xpath
##xpath.find('//title','E:/1439/Jouve india/221690_Streever_Styled.xml')
from lxml import etree
print("running with lxml.etree")
html = etree.Element("html")
body = etree.SubElement(html, "body")
body.text = "TEXT"
print etree.tostring(htmln)

    
