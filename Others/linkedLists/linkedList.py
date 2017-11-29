'''Write a linked list class along with append function(add a node at the end) and destructor function.'''

class Node():
	def __init__(self,value):
		self.value = value
		self.next = None

	def setNext(self,next):
		self.next = next

	def getNext(self):
		return self.next

	def setData(self,value):
		self.value = value

	def getData(self):
		return self.value 

class linkedList():
	def __init__(self):
		self.head = None

	def setHead(self,head):
		self.head = head

	def appendNode(self,value):
		 newNode = Node(value)
		 # newNode.setData(value)
		 #print newNode.getData()
		 if (self.head== None):
		 	self.head = newNode 
		 else:
		 	last = self.head
			while(last.getNext()):
				last  = last.next
			last.setNext(newNode)
	def search(self,value):
		current = self.head
		found = False
		while current != None and not found:
			if (value ==  current.getData()):
				found = True
			current = current.getNext()
		return found

	def removeNode(self,value):
		if(self.search(value)): 
			prev = None
			found =  False
			current = self.head

			while not found:
				if(current.getData() == value):
					found = True
				else:
					prev = current
					current = current.next
			if prev == None:
				self.head = current.getNext()
			else:
				prev.setNext(current.getNext())
		else:
			print "Node doesn't exist."

	def printList(self):
		current = self.head
		#print "here0"
		while (current):
			print current.getData(),
			current = current.getNext()

node1 = linkedList()
node1.appendNode(2)
node1.appendNode(3)
node1.appendNode(4)

node1.printList()
print
# print node1.search(7) 
node1.removeNode(7)
#
node1.printList()