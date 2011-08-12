def metodlain():
     class Binatang(object):
             def __init__(self,kelas):
                     self.kelas = kelas
     def _call(kelas):
             print kelas.nama
	     print kelas.kaler
     return _call

class Ayam(object):
    def __init__(self,nama,kaler):
            self.nama = nama
            self.kaler = kaler
    callme = metodlain()

yam = Ayam('serama','biru')
print yam.callme()# same as Ayam.callme(yam)
