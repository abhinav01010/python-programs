num = int(input("Enter the no of elements: "))
elems = list()
print("Enter the elements in sorted order(ascending)")

for i in range(num):
	elems.append(int(input()))
	
key = int(input("enter the elem to be searched"))
high = num-1
low = 0

while(low<high):
	mid = (low+high)//2
	
	if(key==elems[mid]):
		print("elem found at  pos\n",str(mid))
		break
	elif(key>elems[mid]):
		low = mid +1
		
	else:
		low = mid-1
		
if(low>high):
	print("elem not found")