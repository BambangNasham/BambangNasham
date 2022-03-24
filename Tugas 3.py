barang = []

perintah = 0

while perintah != 7 :
	print(''' 1. menambahkan barang
	2. menghapus barang
	3. mengedit barang
	4. menalpilkan barang
	5. cari barang
	6. cari indeks barang
	7. menampilkan keluaran barang ''')
	perintah = int(input("masukkan perintah :"))
	
	if perintah == 1 :
			while True :
				elemen = (input("masukkan barang :"))
				barang.append(elemen)
				stop = input("ketik F untuk berhenti,selain itu lanjut: ").lower()
				if stop == 'f':
					break
	
	elif perintah == 2 :
		
		while True :
			hapus = int(input("masukkan index yang akan dihapus: "))
			barang.pop(hapus)
			
			stop = input("ketik F untuk berhenti,selain itu lanjut: ").lower()
			if stop == 'f':
				break
		
print(barang)