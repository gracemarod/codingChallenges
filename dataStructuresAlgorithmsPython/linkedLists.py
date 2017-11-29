'''Singly Linked List'''

class Node(object):

	def __init__(self,value):
		self.value = value
		self.next = None

class DoublyLinkedList(object):

	def __init__(self,value):
		self.value = value
		self.prev = None
		self.next = None


a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c


a1 = DoublyLinkedList(a)
a2 =  DoublyLinkedList(b)
a3 = DoublyLinkedList(c)

a.next = b
b.prev = a

b.next = c
c.prev = b
