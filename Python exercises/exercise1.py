myintervals=[]

number=int(input("Enter the number of intervals"))
for i in range(number):
		list1=[]
		min1=int(input("Enter min of the interval"))
		max1=int(input("Enter max of the interval"))
		list1.append(min1)
		list1.append(max1)
	
		myintervals.append(list1)
	
	
print(myintervals)


def recursive_merge(inter, start_index = 0):
    for i in range(start_index, len(inter) - 1):
        if inter[i][1] > inter[i+1][0]:
            new_start = inter[i][0]
            new_end = inter[i+1][1]
            inter[i] = [new_start, new_end]
            del inter[i+1]
            return recursive_merge(inter.copy(), start_index=i)
    return inter    

sorted_on_start = sorted(myintervals)
merged = recursive_merge(sorted_on_start.copy())
print(merged) 

sum = 0
j = 0
for i in range(len(merged)):
	k = merged[j][1]-merged[j][0]
	sum += k
	j += 1

print(sum)	