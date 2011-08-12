import pickle,sys,os,time
import hmac
import hashlib
import binascii
import oauth as oauth
from BeautifulSoup import BeautifulStoneSoup
import urllib2,urllib
import xbmcutils.net
import threading,thread

resource_url = 'http://vimeo.com/api/rest/v2'
#signature_method_hmac_sha1 = oauth.OAuthSignatureMethod_HMAC_SHA1()
encoding_list = ['ascii','latin_1','iso8859_2','iso8859_3','iso8859_4','iso8859_5','iso8859_6','iso8859_7',
		'iso8859_8','iso8859_9','iso2022_jp','iso2022_kr','cp874','gb2312','utf_8']
theVar = 1

class MyThread(threading.Thread):
	def run(self):
		global theVar
		print 'MyThread running'
		print 'So...?'
		print 'This is thread'+str(theVar)+'running'
		theVar += 1

class oAuthSign(object):
	consumer_key = '96aa27766766f260b9e40a356ba9e00d'
	consumer_secret = '325c6b8a2d93561c'
	parameters = None
	http_url = None
	signature_method_hmac_sha1 = oauth.OAuthSignatureMethod_HMAC_SHA1()

	def __init__(self,params,httpUrl):
		self.parameters = params or {}
		self.http_url = httpUrl
	
	def signedURL(self):
		consumer = oauth.OAuthConsumer(self.consumer_key,self.consumer_secret)
		oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer,token=None,http_method='GET',http_url=self.http_url,parameters=self.parameters)
		oauth_request.sign_request(self.signature_method_hmac_sha1,consumer,token=None)
		url = oauth_request.get_normalized_http_url()
		oAuthParams = oauth_request.get_normalized_parameters()
		sign_key = self.signature_method_hmac_sha1.build_signature(oauth_request,consumer,token=None)
		return url+'?'+oAuthParams+'&oauth_signature='+sign_key

def threadFunc(txt,*args):
	print 'Running thread'+txt
		

def fun():
	print "hey"
	return 123456

def getResults(url):
	reqHeader = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10'}
	data = xbmcutils.net.retrieve(url, None, reqHeader)
	return BeautifulStoneSoup(data, convertEntities=BeautifulStoneSoup.HTML_ENTITIES)

def guess_encoding(text):
	for cor_enc in encoding_list:
		try:
			unicode(text,cor_enc,'strict')
		except:
			pass
		else:
			break
	return cor_enc

def decodeIt(text):
	newWord=''
	for c in text:
		try:
			str(c)
			newWord+=c
		except:
			newWord+='?'
	return newWord

print "Hello Fariq"
print time.time()
list = ['1','2','3','4','5']
list[0] = {'id':'value'}
print list[0]['id']
signaturebase = "GET&\
http%3A%2F%2Fvimeo.com%2Fapi%2Frest%2Fv2%2F&\
method%3Dvimeo.videos.search\
%26oauth_consumer_key%3D96aa27766766f260b9e40a356ba9e00d\
%26oauth_nonce%3D1fjwuixisjck1\
%26oauth_signature_method%3DHMAC-SHA1\
%26oauth_timestamp%3D"+str(time.time())
print signaturebase
hashi = hmac.new('key','',hashlib.sha1)
print binascii.b2a_base64(hashi.digest())[:-1]

query = raw_input("search query:")
oAuthSignedUrl = oAuthSign({'method':'vimeo.videos.search','query':query,'full_response':1},resource_url)
print oAuthSignedUrl.signedURL()
print oAuthSignedUrl.http_url
videos = getResults(oAuthSignedUrl.signedURL())
tumnail = []
tumnail = videos.findAll('video')
total = len(tumnail)
print total
print videos('video')[0]['id']
for video in range(total):
	print tumnail[video].get('id')#sfsfgsdg
	print tumnail[video].title.string
	print tumnail[video].thumbnails.thumbnail
	print tumnail[video].thumbnails.thumbnail.next.next.next.next
	print tumnail[video].thumbnails.thumbnail.nextSibling.nextSibling.nextSibling.nextSibling.string
for vid in tumnail:
	print vid.title.string#get child value
	print vid['id']#get attribute
	urllib.urlretrieve(vid.thumbnails.thumbnail.nextSibling.nextSibling.nextSibling.nextSibling.string,os.getcwd()+'/curr.jpg')
	try:
		str(vid.title.string)
	except:
		txt_enc = decodeIt(vid.title.string)
		print txt_enc
		
#print tumnail[0].contents
latin1word = 'Sacr\xe9 bleu!'
unicodeword = unicode(latin1word, 'latin1')
print unicodeword,guess_encoding(latin1word)

for i in range(10):
	thread.start_new_thread(threadFunc,(str(i),))

#consumer = oauth.OAuthConsumer(consumer_key,consumer_secret)
#parameters = {'method':'vimeo.videos.search','query':'test'}
#oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer,token=None,http_method='GET',http_url=resource_url,parameters=parameters)
#oauth_request.sign_request(signature_method_hmac_sha1,consumer,token=None)
#print signature_method_hmac_sha1.get_name()
#print oauth_request.get_normalized_parameters()
#print oauth_request.get_normalized_http_url()
#print oauth_request.get_normalized_http_method()
#print consumer.secret, '!!!!!!consumer secret'
#print oauth_request.get_normalized_parameters()+'&oauth_signature='+signature_method_hmac_sha1.build_signature(oauth_request,consumer,token=None), '!!!!oauth_signature'

a=2
b=4
c=a+b
#print "a=",a,"b=",b,"a+b=",c
while a<10:
	a=a+1
#	print a,
#print 'sys.argv[0]=', sys.argv[0]
#print 'os.getcwd()=', os.getcwd()
#d=raw_input("type something:")
#for huruf in d:
#	print huruf,
#print d

file=open('test','r')
r=pickle.load(file)
#print file.read()
print r
file.close()

#file = open('test','w')
#pickle.dump(d,file)
#file.close()
