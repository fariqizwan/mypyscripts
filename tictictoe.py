import random

def cetakPapan(pap,no):
	print "Pilih lokasi:(Pemain %s)" % str(no)
	print "(1)%s|(2)%s|(3)%s" % (pap[1],pap[2],pap[3])
	print "-----------"
	print "(4)%s|(5)%s|(6)%s" % (pap[4],pap[5],pap[6])
	print "-----------"
	print "(7)%s|(8)%s|(9)%s" % (pap[7],pap[8],pap[9])

def buatPapan(papanItu):
	for i in range(10):
		papanItu.append('')
		
	return papanItu

def ambikLokasi():
	posisi = 0
	print "Pilih posisi:"
	while not (0 < posisi < 10):
		posisi = input()
		
	return posisi

def sapeMulaDulu():
	if (random.randint(0,1)):
		return "pemain1"
	else:
		return "pemain2"
		
def hurufPemain():
	huruf = ''
	while not (huruf == 'O' or huruf == 'X'):
		print "Pilih simbol pilihan anda: (O atau X)->"
		huruf = raw_input().upper()
	
	if huruf == 'O':
		return 'O','X'
	else:
		return 'X','O'

def menangKe(hur,papan):
	return ((papan[1]==hur and papan[2]==hur and papan[3]==hur)
		or (papan[4]==hur and papan[5]==hur and papan[6]==hur)
		or (papan[7]==hur and papan[8]==hur and papan[9]==hur)
		or (papan[1]==hur and papan[4]==hur and papan[7]==hur)
		or (papan[2]==hur and papan[5]==hur and papan[8]==hur)
		or (papan[3]==hur and papan[6]==hur and papan[9]==hur)
		or (papan[1]==hur and papan[5]==hur and papan[9]==hur)
		or (papan[7]==hur and papan[5]==hur and papan[3]==hur))
		
while True:
	papan = []
	papan = buatPapan(papan)
	pemain1,pemain2 = hurufPemain()
	print "Pemain 1 = %s, Pemain 2 = %s" % (pemain1,pemain2)
	sdgMain = True
	sapeJalan = sapeMulaDulu()
	print "%s akan mulakan dulu.." % sapeJalan
	
	while sdgMain:
		if (sapeJalan == 'pemain1'):
			cetakPapan(papan,1)
			indeks = ambikLokasi()
			papan[indeks] = pemain1
			if menangKe(pemain1,papan):
				print "Pemain 1 menang!!"
				sdgMain = False
			else:
				sapeJalan = 'pemain2'
		
		elif (sapeJalan == 'pemain2'):
			cetakPapan(papan,2)
			indeks = ambikLokasi()
			papan[indeks] = pemain2
			if menangKe(pemain2,papan):
				print "Pemain 2 menang!!"
				sdgMain = False
			else:
				sapeJalan = 'pemain1'
	
	print "Adakah anda ingin meneruskan permainan sekali lagi?(y/n)"
	terus = ''
	while not (terus == 'y' or terus == 'n'):
		terus = raw_input()
		
	if terus == 'n':
		break
	
	
	
	
