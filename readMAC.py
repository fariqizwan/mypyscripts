fileRead = open('macAdd.txt','r')
fileWrite = open('macAddNew.txt','w')

for line in fileRead:
	charList = list(line)
	index = 2
	for i in range(len(charList)/2-1):
		charList.insert(index,':')
		index+=3
	print str(charList)
	newMac = ''
	for a in charList:
		newMac += a
	print newMac
	fileWrite.write(newMac)

fileRead.close()
fileWrite.close()
