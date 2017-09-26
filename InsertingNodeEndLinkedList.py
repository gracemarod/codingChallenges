# From Firecode.io
# Inserting a Node at the End of a Singly Linked List
# Write a function to insert a node at the end of a Singly Linked-List.


class Node:
	def __init__(self):
		self.data = None
		self.next = None

	def setData(self,data):
		self.data = data

	def getData(self):
		return self.data

	def setNext(self,next):
		self.next = next

	def getNext(self):
		return self.next

class SinglyLinkedList:
	#constructor
	def __init__(self):
		self.head = None

	#method for setting the head of the node
	def setHead(self,head):
		self.head = head
    
	def insertAtEnd(self,data):
        #Make new node and set the data as head
		newNode = Node()
		newNode.setData(data)
        
        #Check if node is empty
		if self.head == None:
			self.head = newNode
        else:
			last = self.head
            #Iteriate through old node until reach the end
			while(last.getNext()):
				last = last.next
            #point the last node to the newNode (new data)
			last.next = newNode