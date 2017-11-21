import re
#print re.split(r'\s*','hey    u r using re modules')
#print re.split(r'(\s*)','hey    u r using re modules')
#print re.split(r'(s*)','hey    u r using re modules')
#print re.split(r'[a-f]','hey    u r using re modules')
#print (re.split(r'[a-fA-F]','hey    u r using RE modules',re.I|re.M))
#print re.split(r'[a-f][a-f]','heay    u r using re modules')
#print re.split(r'\d','hey u r using re1234 modules')
#print re.split(r'\d*','hey u r using re1234 modules')
print re.split(r'(\d*)','hey u r using re1234 modules')
print re.findall(r'\d+','hey u r using re1234 modules5678')
print (re.findall(r'\d{1,5}\s\w+','feqenen324 main st.iewasd',re.I|re.M))
print (re.findall(r'\d{1,5}\s\w+\s\w+\.','feqenen324 main st.iewasd',re.I|re.M))

exampleString = '''
Jessika is 15 years old, and Danel is 27 years old, Edward is 101 years old
'''
age = re.findall(r'\d{1,3}',exampleString)
names = re.findall(r'[A-Z][a-z]*',exampleString)
print age,names

ageDict = {}
x = 0
for eachName in names:
	ageDict[eachName] = age[x]
	x += 1
print ageDict	