class Node(object):
	def __init__(self,data):
		self.data = data
		self.next = None
	def __str__(self):
		return "address of %s"%self.data

class Slink(object):
	def __init__(self):
		self.head = None

	def addFirst(self,data):
		node = Node(data)
		if self.head == None:
			self.head = node
		else:
			node.next = self.head
			self.head = node
	def printAll(self):
		current = self.head
		while current != None:
			print ("{[%s]|[%s]}->"%(current.data,current.next),)
			current = current.next

	def reverse(self):
		last = None
		current = self.head
		while(current):
			temp = current.next
			current.next = last
			last = current
			current = temp
		self.head = last

if __name__ == "__main__":
	o=Slink()
	o.addFirst(10)
	o.addFirst(20)
	o.addFirst(30)
	# o.addFirst(40)
	# o.addFirst(50)
	# o.addFirst(60)
	o.printAll()
	print ("-----------------")
	o.reverse()
	o.printAll()
