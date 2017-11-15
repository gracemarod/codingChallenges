'''2.6 Implement a function to check if a linked list is a Palindrome.'''

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
			print curr.getData()
			curr = curr.getNext()
	def getToMiddle(self):
		slow_ptr = self.head
		fast_ptr = self.head

		if fast_ptr != None:
			while (fast_ptr != None and fast_ptr.getNext() != None):
				fast_ptr = fast_ptr.getNext().getNext()
				slow_ptr = slow_ptr.getNext()

			if fast_ptr != None:
				midnode = slow_ptr
				slow_ptr = slow_ptr.getNext()

		print "The middle Node is", slow_ptr.getData()

myList = UnorderedList()
myList.add("r")
myList.add("a")
myList.add("d")
myList.add("a")
myList.add("r")

myList.printList()
myList.getToMiddle()
