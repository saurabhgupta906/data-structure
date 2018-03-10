class Node(object):
	def __init__(self,data):
		self.data = data
		self.next = None
	def __str__(self):
		return "address of %s"%self.data

class Slink(object):
	def __init__(self):
		self.head = None
		self.tail = None

	def addFirst(self,data):
		node = Node(data)
		if self.head == None:
			self.head = node
			self.tail = node
		else:
			node.next = self.head
			self.head = node
	def insertLast(self,data):
		node = Node(data)
		if self.head == None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node

	def printAll(self):
		current = self.head
		while current != None:
			print "{[%s]|[%s]}->"%(current.data,current.next),
			current = current.next


o = Slink()
o.addFirst(0)
o.addFirst(1)
o.addFirst(12)
o.addFirst(13)
o.addFirst(14)
o.addFirst(110)
# o.insertLast(210)
o.printAll()