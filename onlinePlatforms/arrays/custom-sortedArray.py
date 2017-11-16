'''Sort the array so all the even numbers are first and the 
odd numbers are last. The program should return the minium
number of required swaps for the array to be custom sorted.
'''

def customSort(arr):
	left = 0 
	right = len(arr)-1
	count =0
	
	while left < right:
		print "left ", arr[left], "right: ", arr[right]

		#Increment left index while the element it's even
		while (arr[left] % 2 ==0  and left<right ):
			left+=1
			print "Left: ", arr[left], left

		#Increment left index while the element it's odd
		while (arr[right]%2==1 and left<right):
			right -= 1
			print "right: ", arr[right], right

		#Now we have the elements we need to swap as 
		#long as left index is less than right index
		if (left <right):
			count+=1
			arr[left],arr[right] = arr[right],arr[left]
			left += 1
			right -= 1
		
		print arr
		print "Count: ", count
	return count

l = [5,8,5,11,4,6]
customSort(l)















l = [16,4,3,5]
