class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class Linkedlist:
	def __init__(self):
		self.head = None

	def insert(self, data):
		new_node = Node(data)
		#new_node.data = data
		new_node.next = self.head
		self.head = new_node

	def search(self, item):
		curr = self.head
		while(curr):
			if curr.data == item:
				return True
			curr = curr.next
		return False

	def delete(self, item):
		curr = self.head
		if self.head.data == item:
			temp = self.head
			self.head = self.head.next
			temp.next = None
		while(curr != None and curr.next != None):
			if curr.next.data == item:
				print("Item deleted")
				curr.next = curr.next.next
			curr = curr.next
			
	
	def printll(self):
		curr = self.head
		while(curr):
			print(curr.data)
			curr = curr.next


"""ll = Linkedlist()
ll.insert(4)
ll.insert(1)
ll.insert(20)
ll.insert(12)

ser = ll.search(21)
print(ser)

del1 = ll.delete(20)
print(del1)

ll.printll()"""












