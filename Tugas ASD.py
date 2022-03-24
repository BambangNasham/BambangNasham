barang = []

perintah = 0

while perintah != 'stop' :
	print(''' 1. menambah barang
	2. menghapus barang
	3. mengedit barang
	4. menampilkan barang
	5. cari barang
	6.mencari index
	7.keluaran : ''')
	
if perintah == '1' :
	nama_barang = int (input("masukkan nama barang :"))
	barang.append (nama_barang)
	
elif perintah == '2' :
	index = int (input("masukkan index yang akan dihapus :"))
	
elif perintah == '3' :
	barang1 = int (input("masukkan barang yang dicari"))
	barang [barang1] = input ("masukkan barang baru :")
	
elif perintah == '4' :
	print(barang)
	
elif perintah == '5' :
	cari = input ("masukkan barang yang dicari :")
	if cari in barang :
		print ("barang ditemukan")
	else :
		print ("barang tidak ditemukan")
		
elif perintah == '6' :
		cari = input ("masukkan barang yang dicari :")
		if cari in barang :
			print (buah.index(cari))
		else :
			print ("barang tidak ditemukan")