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

#Class for linked list
class UnorderedList():
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

#Function to add more nodes
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

#Certain for a specific node
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

#Checks if the linked list is a palindrome, by attaching all the strings to an array
#and comparing the original array with the reversed array

	def isPalindrome(self):
		node = self.head
		arr = []

		while node:
			arr.append(node.getData())
			node = node.getNext()

		if self.isPalindromeList(arr):
			self.printList(), 
			print "is a palindrome."
		else:
			self.printList(),
			print "is NOT a palindrome."

	def isPalindromeList(self,string):
		return string == string[::-1]



list1 = UnorderedList()

#The last added node is going to be the head, so in the case of a string, 
#the last character in the string is added first and the first char of the string
#is added first
list1.add("r")
list1.add("a")
list1.add("d")
list1.add("a")
list1.add("r")

list1.isPalindrome()

list2 = UnorderedList()
list2.add("l")
list2.add("l")
list2.add("a")
list2.add("b")

list2.isPalindrome()

