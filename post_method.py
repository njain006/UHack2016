import requests
import time
url = 'https://triggers.octoblu.com/flows/cb56918f-c732-43ac-9ef8-48d48647161d/triggers/6edae520-d80a-11e5-a16a-f91c0dcd61e1'
names = [ '#citrix','#ibm','#twitter', '#capitolone','#dell' ]

i=0
print (i)
print (names[0])
while i < 5:	
	print (i,names[i])

	# POST with form-encoded data
	r = requests.post(url, data= {'company':names[i]})


	# Response, status etc
	print (r.text)
	print (r.status_code)
	i = i+1
	time.sleep(120)