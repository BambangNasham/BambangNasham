nama_barang = []
maksimal_nama_barang = int(input("masukkan maksimal nama barang: "))
def isFull():
  if len(nama_barang) == maksimal_nama_barang:
    print("barang penuh")
    return True
  return False

def enqueue():
  if isFull() == False:
    d = input("tambahkan baru baru: ")
    nama_barang.append(d)
    print("barang yang telah ditambahkan : ", d)
    
def isEmpty():
  if len(nama_barang) == 0:
    print("nama barang kosong")
    return True
  return False

def dequeue():
  if isEmpty() == False:
    print(nama_barang.pop(0),"di hapus")


menu = 0
while menu !=5:
  print('''
  a.enqueue > menambah nama barang
  b. dequeue > menghapus barang
  c. Full > mengecek nama barang apakah penuh
  d. size > melihat ukuran barang
  e. stop''' )

  menu = input("masukkan menu pilihan: ")

  if menu == 'a':
    enqueue()
  elif menu == 'b':
    dequeue()
  elif menu == 'c':
    if isFull() == False:
      print("barang belum terisi penuh")
  elif menu == 'd':
    print("barang saat ini terisi: ",len(nama_barang),"\n maksimal barang : ",maksimal_nama_barang)
  elif menu == 'e':
    break