text_file = open("textfile.txt", "r")

array= text_file.read().split(" ")
text_file.close()
print(array)


newarray=[]
x=0
k=0
list1=[]
for i in range(len(array)):
	
			
			s=array[i]
			list1.append(s)
			k+=1
			if k==3:
				newarray.append(list1)
				k=k-3
				list1=[]
print (newarray)	
		



	