import re.urllib
#re module used here on web scrapp
try:
	import urllib.request
except:
    pass
sites = 'google gmail'.split()
for site in sites:
	print("searching for" + site)
	try:
		u = urllib.urlopen("http://" + s  + ".com")
	except:
		u = urllib.request.urlopen("http://" + s  + ".com")
	text = u.read()
	title = re.findall(r'<title>+.*<title>+', re.I|re.M , str(text))
	print title[0]	
		

