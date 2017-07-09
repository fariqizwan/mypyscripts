import os,gzip,shutil,re,sys
import subprocess
#import getopt


def readFileCountStatus(thefile):
	try:
                if thefile.endswith('gz'):
                        print "filename: %s" % thefile
                        rem = re.compile('^[RSTQPU]')
                        k = ['R','S','T','Q','P','U']
                        rlist = []
                        fcont = gzip.open(thefile,'r')
                        cnt = 0
			aidnum = ''
                        for line in fcont:
                                q = rem.findall(line)
                                rlist.extend(q)
				if line.find('aid:') == 0:
					aidnum = line.strip('aid: ').strip('\n')
                        slist = sorted(((i,rlist.count(i)) for i in k),key = lambda k:k[1],reverse=True)
			total_sent = 0
			soft_bounce = 0
			hard_bounce = 0
                        for status,count in slist:
				print "%s = %d" % (status,count)
				if status in ['R','S','T']:
					total_sent += count
				if status == 'T':
					soft_bounce = count
				elif status == 'S':
					hard_bounce = count
			print "AID for this mailing is = %s" % aidnum
			print "Total sent = %d" % total_sent
			renamefile(thefile,aidnum,total_sent,soft_bounce,hard_bounce)
			print '~~'*10
                        fcont.close()
        finally:
		pass

def getaidfrompid(pid='2103710041'):
	getmid = subprocess.Popen(['./testgetmid.sh',str(pid)],stdout=subprocess.PIPE)
	output,err = getmid.communicate()
	return output

def renamefile(fname,aid,tot_sent,soft,hard):
	name,ftype = fname.split('.')
	wostart,pid,woseq = name.split('_')
	#aidcheck = getaidfrompid(pid).strip('\n')
	newname = "%s:%s_%s_%d_%d_%d" % (name,str(int(wostart)+1),aid,tot_sent,soft,hard)
	print "New name for the file: %s" % newname
	agree = raw_input("Do you want to move this file?(y/n)")
	if agree == 'y':
		movefiletodonetmp(fname,newname)
	else:
		print "Cancel moving the file"

def movefiletodonetmp(filename,newfilename):
	#with gzip.open(filename,'r') as zfile, open('donetmp/%s' % newfilename,'w') as uzfile:
	#	shutil.copyfileobj(zfile,uzfile)

	zfile = gzip.open(filename,'r')
	uzfile = open('../donetmp/%s' % newfilename,'w')
	try:
		shutil.copyfileobj(zfile,uzfile)
	finally:
		zfile.close()
		uzfile.close()
		
#def help():
#	print "./reportstatus.py --mta=<mtamachinenumber>"
#	print "./reportstatus.py --justrun (Run this tool in current directory-for testing purpose"

def main(argv):
	#try:
	#	opts,args = getopt.getopt(argv,'',['mta=','justrun'])
	#	if args:
	#		print args
	#	else:
	#		help()
	#except getopt.GetoptError:
	#	help()
	#	sys.exit()
	#for opt,arg in opts:
	#	if opt in ("--mta"):
	#		print "Mta to log into is: %s" % arg
	#	elif opt in ("--justrun"):
	for f in os.listdir('.'):
		readFileCountStatus(f)
	#	else:
	#		help()

if __name__ == '__main__':
	main(sys.argv[1:])
