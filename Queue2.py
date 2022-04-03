queue = []
max_size = int(input("Masukkan Ukuran Maksimal Queue: "))

def isEmpty():
	if len(queue) == 0:
		print("Queue Kosong.")
		return True
	return False
	
def isFull():
	if len(queue) == max_size:
		print("Queue Penuh.")
		return True
	return False
		
def dequeue():
	if isEmpty() == False:
		print(queue.pop(0), "terhapus dari queue.")

def enqueue():
	if isFull() == False:
		x = input("Masukkan Antrian Baru: ")
		queue.append(x)
		print(x, "ditambahkan ke queue.")

p = 0
while p != '6':
    print('''\n1. Enqueue => Menambah Antrian
2. Dequeue => Menghapus dari Antrian
3. Full => Memeriksa Apakah Queue Penuh
4. Size => Melihat Ukuran Queue''')
    p = input("Ketik 6 untuk berhenti\nMasukkan Perintah: ")
    print()
    
    if p == '1':
    	enqueue()
    elif p == '2':
    	dequeue()
    elif p == '3':
    	if isFull() == False:
    		print("Queue belum penuh.")
    elif p == '4':
    	print("Ukuran queue saat ini: ", len(queue), "\nUkuran maksimal queue: ", max_size)