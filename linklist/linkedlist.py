class Link(object):
	def __init__(self,data):
		self.data = data
		self.next = None
class LinkList(object):
	def __init__(self):
		self.head = None
		self.tail = None
	def insertFirst(self,data):
		node = Link(data)
		if self.head == None:
			self.head = node
			self.tail = node
		else:
			node.next = self.head
			self.head = node
	def printAll(self):
		current = self.head
		while current != None:
			print current.data
			current = current.next
	def reverseLinkList(self):
		last = None
		current = self.head
		while current != None:
			temp = current.next
			current.next = last
			last = current
			current = temp
		self.head = last

o = LinkList()
o.insertFirst(10)
o.insertFirst(20)
o.insertFirst(30)
o.insertFirst(40)
o.insertFirst(50)
o.printAll()
print "----------"
print o.head.data
print o.tail.data
print "----------"
o.reverseLinkList()
o.printAll()
