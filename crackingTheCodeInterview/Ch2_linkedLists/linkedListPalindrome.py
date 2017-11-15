'''2.6 Implement a function to check if a linked list is a Palindrome.'''

# Create the node
class Node():
	def __init__(self,initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self,newData):
		self.data = newData

	def setNext(self,newNext):
		self.next = newNext


class UnorderedList():
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self,item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head=temp

	def size(self):
		current = self.head
		count = 0 
		while current != None:
			count +=1
			current = current.getNext()
		return count

	def search(self,item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
		return found

	def remove(self,item):
		current = self.head
		prev = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else:
				prev = current
				current = self.getNext()
		if prev == None:
			self.head = current.getNext()
		else:
			prev.setNext(current.getNext())

	def printList(self):
		curr = self.head
		while curr:
			print curr.getData(),
			curr = curr.getNext()

	def isPalindrome(self):
		node = self.head
		arr = []

		while node:
			arr.append(node.getData())
			node = node.getNext()

		return self.isPalindromeList(arr)

	def isPalindromeList(self,string):
		return string == string[::-1]



myList = UnorderedList()
myList.add("b")
myList.add("i")
myList.add("t")
myList.add("c")
myList.add("h")

# myList.printList()
if myList.isPalindrome():
	myList.printList(),
	print "is a palindrome."
else:
	myList.printList(), 
	print "is NOT a palindrome."
# myList.reverseList()
# print
# myList.printList()
