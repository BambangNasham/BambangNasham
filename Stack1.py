#stack
def bikin_stack () :
		stack = [38,39,40]
		return stack
		
def periksa_empty ( stack ) :
		return len (stack) == 0
		
def push ( stack,item ):
		stack.append (item)
		print ("ukuran :",item)
		
def pop (stack) :
		if (periksa_empty (stack)) :
			return print ("ukuran sepatu pada rak kosong")
		print ("ukuran sepatu yang diambil:",stack.pop())
		
def size (stack) :
		print ("jumlah sepatu pada rak:" ,len(stack))
		
def top (stack):
		top = len (stack) -1
		if top < 0 :
			print (" tidak terdefenisi")
		else :
			print ("ukuran sepatu yang teratas:" , stack [top])
			
def tampilkan (stack) :
		print (stack)
		
			
s = bikin_stack ()
print (" tumpukan ukuran sepatu pada rak ")


#Data awal stack
print ("ukuran sepatu yang yang berada pada tumpukan saat ini:  ",s) 

size (s)
top (s)
print ()

#Meminjam ukuran sepatu
pop (s)
pop (s)
pop (s)
print ("ukuran sepatu yang yang berada pada tumpukan saat ini:  ",s) 
top (s)
size (s)
print ()

#Mengembalikan ukuran sepatu
push (s,input())
push (s,input())
push (s,input ())
print ("ukuran sepatu yang yang berada pada tumpukan saat ini:  ",s)