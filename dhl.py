import requests, re, bs4, sys

def dhl(start, finish):
	#3394405626 известный номер

	for track in range(start, finish):
		url = 'https://www.dhl.ru/shipmentTracking?AWB='+str(track)
		s=requests.get(url)
		b=bs4.BeautifulSoup(s.text, "html.parser")
	
		b=str(b)
		b=b.replace('\n','')
		b=re.sub(r'\s+', ' ', b)
	
		index_error = b.find('404')
		error = b[index_error:index_error+3]
		
		if error != '404':
			start_from = b.find('"origin" : { "value" : "') + 24
			end_from = b.find('", "label" : "Origin Service Area"', start_from)
			start_dest = b.find('"destination" : { "value" : "') + 29
			end_dest = b.find('", "label" : "Destination Service Area"', start_dest)
			print ("NUMBER: "+str(track)+" FROM: "+b[start_from:end_from]+" - TO: "+b[start_dest:end_dest])
		#else: 
			#print ("NUMBER: "+str(track)+" NOT FOUND")

cont="y"
while (cont != 'n'):
	sys.stdout.write('Начало диапазона: ') ,
	start=int(input())
	sys.stdout.write('Конец  диапазона: ') ,
	finish=int(input())
	
	dhl(start, finish)
	sys.stdout.write('Ввести новый диапазон?(y/n)') ,
	cont=input()
	cont=cont.lower()

#Последние диапазоны 4606505492 4606506122 4890425061 4890425573 4890426796

#pattern = '\"destination\":{\"value\":\"(.*?)\",\"label\":\"DestinationServiceArea\"'

'''
pattern = '"destination" : { "value" : "(.+?)", "label" : "Destination Service Area"'
destination=re.search(pattern, b)

print (destination)


if destination:
    found = destination.group(1)
'''

#print b.index(pattern)
#print (pattern)
#destination=re.search(pattern, str(b))
#print (destination.group(0))
#print('Destination :' + destination[0])
