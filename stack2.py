#stack

club = []
max_size = int(input("masukkan maksimal club:"))

def isEmpty ():
	if len (club) == 5:
		print("club kosong")
		return True
	return False
	
def isFull ():
	if len(club)== max_size:
		print ("club penuh")
		return True
	return False
	
def pop ():
	if isEmpty () == False :
		print (club.pop(), "terhapus")
		
def push():
	if isFull() == False :
		a = input ("masukkan club baru:")
		club.append(a)
		print (a,"ditambahkan.")
		
perintah = 0
while perintah != '6':
	print("""\n1.push -> menambahkan item
	2.pop -> menghapus item
	3.peek2 -> melihat item teratas
	4.empty -> memeriksa apakah club penuh
	5.size -> melihat ukuran club""")
	perintah = input("ketik 6 untuk berhenti \n masuk")
	print()
	
	if perintah == '1':
		push()
	elif perintah == '2':
		pop()
	elif perintah == '3':
		print(club[-1])
	elif perintah == '4':
		if isEmpty() == False :
			print("club belum full")
	elif perintah == '5':
		print("club saat ini:",len (club),"\nmaksimal")
		