'''Input: An array of values and a value k. Print out the pairs whose sum equal val k'''
import time

max_num = 100

def printPairsHash(arr,k):
	print "input: ", arr
	binmap = [0]* max_num
	for i in range(0,len(arr)):
		temp = k - arr[i]
		
		
		if (temp >= 0 and binmap[temp]==1):
			print arr[i], ",", temp

		#print "arr: ", arr[i]	
		binmap[arr[i]]=1
		#print "map: ", binmap	
		

def printPairsSorting(arr,k):
	sortedArr = []
	for t in arr:
		if t not in sortedArr:
			sortedArr.append(t)
	sortedArr = sorted(sortedArr)

	for i in range(0,len(sortedArr)):
		for j in range(i,len(sortedArr)):	
			if sortedArr[i] + sortedArr[j] == k:
				print sortedArr[i], ",", sortedArr[j]

arr = [1, 5, 7, -1]
k = 6
arr = [10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1]
k = 11

# start_time = time.time()
printPairsSorting(arr,k)
# print "--- %s seconds for Sorting ---" % (time.time() - start_time)

#start_time = time.time()
printPairsHash(arr,k)
#print "--- %s seconds for Sorting ---" % (time.time() - start_time)

