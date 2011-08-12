import threading,thread
import time
import urllib2,urllib
import os

threadBreak = False
link = []
link.append('http://b.vimeocdn.com/ts/239/367/23936716_640.jpg')
link.append('http://b.vimeocdn.com/ts/299/860/29986040_640.jpg')
link.append('http://b.vimeocdn.com/ts/299/860/29986013_640.jpg')
link.append('http://b.vimeocdn.com/ts/693/406/69340658_640.jpg')
link.append('http://b.vimeocdn.com/ts/239/368/23936891_640.jpg')
link.append('http://b.vimeocdn.com/ts/868/243/86824368_640.jpg')
link.append('http://b.vimeocdn.com/ts/587/743/58774363_640.jpg')
link.append('http://b.vimeocdn.com/ts/587/829/58782922_640.jpg')
link.append('http://b.vimeocdn.com/ts/588/371/58837123_640.jpg')
link.append('http://b.vimeocdn.com/ts/132/201/13220123_640.jpg')
link.append('http://b.vimeocdn.com/ts/210/717/21071794_640.jpg')
link.append('http://b.vimeocdn.com/ts/214/619/21461986_640.jpg')
link.append('http://b.vimeocdn.com/ts/290/985/29098527_640.jpg')
link.append('http://b.vimeocdn.com/ts/337/956/33795660_640.jpg')
link.append('http://b.vimeocdn.com/ts/424/014/42401463_640.jpg')
link.append('http://b.vimeocdn.com/ts/440/745/44074556_640.jpg')
link.append('http://b.vimeocdn.com/ts/587/852/58785252_640.jpg')
link.append('http://b.vimeocdn.com/ts/657/545/65754583_640.jpg')
link.append('http://b.vimeocdn.com/ts/664/022/66402289_640.jpg')
link.append('http://b.vimeocdn.com/ts/664/685/66468591_640.jpg')
link.append('http://b.vimeocdn.com/ts/726/581/72658180_640.jpg')
link.append('http://b.vimeocdn.com/ts/791/068/79106817_640.jpg')
link.append('http://b.vimeocdn.com/ts/481/003/48100333_640.jpg')
link.append('http://b.vimeocdn.com/ts/394/826/39482618_640.jpg')
link.append('http://b.vimeocdn.com/ts/642/846/64284634_640.jpg')
link.append('http://b.vimeocdn.com/ts/951/257/95125731_640.jpg')
link.append('http://b.vimeocdn.com/ts/633/504/63350470_640.jpg')
link.append('http://b.vimeocdn.com/ts/214/609/21460924_640.jpg')
link.append('http://b.vimeocdn.com/ts/256/935/25693567_640.jpg')
link.append('http://b.vimeocdn.com/ts/873/947/87394721_640.jpg')
link.append('http://b.vimeocdn.com/ts/729/719/72971986_640.jpg')
link.append('http://b.vimeocdn.com/ts/586/329/58632961_640.jpg')
link.append('http://b.vimeocdn.com/ts/766/724/76672457_640.jpg')
link.append('http://b.vimeocdn.com/ts/794/241/79424182_640.jpg')
link.append('http://b.vimeocdn.com/ts/776/090/77609007_640.jpg')
link.append('http://b.vimeocdn.com/ts/896/492/89649266_640.jpg')
link.append('http://b.vimeocdn.com/ts/730/181/73018120_640.jpg')
link.append('http://b.vimeocdn.com/ts/209/144/20914495_640.jpg')
link.append('http://b.vimeocdn.com/ts/209/394/20939461_640.jpg')
link.append('http://b.vimeocdn.com/ts/356/498/35649843_640.jpg')
link.append('http://b.vimeocdn.com/ts/431/433/43143369_640.jpg')
link.append('http://b.vimeocdn.com/ts/758/891/75889174_640.jpg')
link.append('http://b.vimeocdn.com/ts/436/285/43628592_640.jpg')
link.append('http://b.vimeocdn.com/ts/920/532/92053235_640.jpg')
link.append('http://b.vimeocdn.com/ts/143/357/14335738_640.jpg')
link.append('http://b.vimeocdn.com/ts/455/936/45593621_640.jpg')
link.append('http://b.vimeocdn.com/ts/455/957/45595735_640.jpg')
link.append('http://b.vimeocdn.com/ts/455/957/45595779_640.jpg')
link.append('http://b.vimeocdn.com/ts/457/765/45776542_640.jpg')
link.append('http://a.vimeocdn.com/thumbnails/defaults/default.300x400.jpg')

def TimeProcess():
	print (time.time() - startTime)

class Mythread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	
	def run(self):
		for h in range(1000):
			res=0
			for i in range(1000):
				res+=1
		print str(res) + ' in thr'

def withoutThread():
	for h in range(1000):
		res=0
		for i in range(1000):
			res+=1
	print str(res) + ' 1'
	for h in range(1000):
		res=0
		for i in range(1000):
			res+=1
	print str(res) + ' 2'

def withThread():
	thr1=Mythread()
	thr2=Mythread()

	thr1.start()
	thr2.start()

	thr1.join()
	thr2.join()

def usingStartThread(t,*args):
	for h in range(1000):
		res=0
		for i in range(1000):
			res+=1
	print str(res) + ' in usingStThr'+str(t)

def getImageWithoutThread():
	start = time.time()
	for i in range(len(link)):
		urllib.urlretrieve(link[i],os.getcwd()+'/media/'+str(i)+'-%.3f' % (time.time()-start)+'.jpg')

def getImageWithThread(index,*args):
	urllib.urlretrieve(link[index],os.getcwd()+'/mediaUT/'+str(index)+'-%.3f' % (time.time()-args[0])+'t.jpg')
	print index,


'''startTime = time.time()
withoutThread()
endTime = time.time()

print 'Loop without thread took %.3f' % (endTime-startTime)'''

startTime = time.time()
withThread()
endTime = time.time()

print 'Loop with thread took %.3f' % (endTime-startTime)

startTime = time.time()
thread.start_new_thread(usingStartThread,(1,))
thread.start_new_thread(usingStartThread,(2,))
endTime = time.time()

print 'Loop with usingStartThreadthread took %.3f' % (endTime-startTime)

startTime = time.time()
getImageWithoutThread()
endTime = time.time()

print 'Retrieve image without thread took %.3f' % (endTime-startTime)

startTime = time.time()
for i in range(len(link)):
	thread.start_new_thread(getImageWithThread,(i,startTime))
	#print i,
endTime = time.time()

print 'Retrieve image with thread took %.3f' % (endTime-startTime)

raw_input()
threadBreak = True
quit()

'''thr = threading.Thread(target = TimeProcess)
thr.start()
thr.join()'''
