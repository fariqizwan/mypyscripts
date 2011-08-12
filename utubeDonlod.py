import urllib2,urllib
import re
import sys,time
import pickle
import uuid,os,tempfile
from BeautifulSoup import BeautifulSoup

videoTitle = ''
#Hi githubbers
def main(argv=None):
	global videoTitle
	if argv is None:
		argv = sys.argv
	link = argv[1].split('&')#clean the url so we took only the url without any parameters
	startTime = time.time()
	theSource = getHTMLSource(link[0])
	soup = BeautifulSoup(theSource)
	vidTitle = soup.findAll(id="eow-title")
	print vidTitle[0].get('title')
	videoTitle = vidTitle[0].get('title')
	getDownloadLink(theSource)
	endTime = time.time()-startTime
	print "Time taken = %.3f" % endTime

def getHTMLSource(link):
	source = ''
	usrAgent = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10'}
	request = urllib2.Request(link,headers=usrAgent)
	urllink = urllib2.urlopen(request)
	while True:
		data = urllink.read(1024)
		if data == "":
			break
		source += data 
	
	urllink.close()
	#file1 = open('tubi','w')
	#file1.write(source)
	return source

def getFileInfo(resLink):
	vidFile = urllib2.urlopen(resLink)
	print vidFile.info().getsubtype() #see http://docs.python.org/library/urllib2.html and http://docs.python.org/library/mimetools.html#mimetools.Message for reference
	print vidFile.info().getplist()

def getDownloadLink(source):
	videoUrllist = []
	#URLlist = re.findall('"fmt_url_map": "([^"]+)"',source)#Can't be use anymore as of 4/8/2011
	URLlist = re.findall('"url_encoded_fmt_stream_map": "([^"]+)"',source)
	split1 = URLlist[0].split(',')
	print len(split1)
	for s in split1:
		ar1 = s.split('url=')
		ar2 = ar1[1].split('\\u0026')
		print urllib.unquote(ar2[0]),ar2[len(ar2)-1].split('itag=')[1]
		theUrl = urllib.unquote(ar2[0])
		theItag = int(ar2[len(ar2)-1].split('itag=')[1])
		if theItag < 40 and theItag != 35:
			videoUrllist.append({'url':urllib.unquote(ar2[0]),'itag':ar2[len(ar2)-1].split('itag=')[1]})
	
	#print 'HQ-------------->'+split1[0]#this is for the HQ
	#print 'MQ-------------->'+split1[1]#this is for the MQ
	#print 'LQ-------------->'+split1[2]#this is for the LQ
	#print 'WQ-------------->'+split1[5]#this is for the WQ
	
	#Can't be use anymore as of 4/8/2011
	'''for i in range(len(split1)):
		print split1[i].split('|')[0]
		if int(split1[i].split('|')[0]) < 40 and not 35:
			print split1[i].split('|')[1].decode('raw_unicode_escape').replace('\\','')
			videoUrllist.append(split1[i].split('|')[1].decode('raw_unicode_escape').replace('\\',''))'''
	
	#split2 = split1[0].split('|')
	
	#downloadUrl = split2[1].replace('\\','')
	#print downloadUrl
	theVid = ''
	print videoTitle

	tempfile.tempdir = os.path.join(os.getcwd(),'temp')
	temp = tempfile.NamedTemporaryFile(prefix=str(uuid.uuid4())+'_')
	print temp.name
	#os.path.getmtime(temp.name) #get time from last modification of the file
	
	'''videoCon = urllib2.urlopen(videoUrllist[-1])
	#vidFile = open(temp,"w+b")
	filesize = 0
	while True:
		viddata = videoCon.read(1024)
		filesize += len(viddata)
		if viddata == "":
			print "%.2f Mb" % (filesize/1024.0/1024.0)
			break
		#theVid += viddata
		#vidFile.write(viddata)
		temp.write(viddata)
	
	videoCon.close()
	
	d=raw_input("type something:")'''
	
	#vidFile = open("lala.flv","wb")
	#pickle.dump(theVid,vidFile)
	
	for vid in videoUrllist:
		print vid['url']
		getFileInfo(vid['url'])

if __name__ == '__main__':
	main()
