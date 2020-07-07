from linkedlist import Linkedlist

hash_table = [None] * 13

class Hashing():
	def hash_calculator(self, num):
		return num % 13


	def insert(self, lst):
		for i in lst:
			mapping = self.hash_calculator(i)
			# print("mapping:", mapping)
			if hash_table[mapping] == None:
				#print("Creating new linkedlist ", i)
				ll = Linkedlist()
				hash_table[mapping] = ll
			else:
				ll = hash_table[mapping]
			if not ll.search(i):
				# print("inserting elemen t", i)
				ll.insert(i)
				# ll.printll()

	def search(self, item):
		mapping = self.hash_calculator(item)
		if hash_table[mapping]:
			return hash_table[mapping].search(item)
		return False

	def delete(self, item):
		mapping = self.hash_calculator(item)
		if hash_table[mapping]:
			 hash_table[mapping].delete(item)
		




def main():
	hh = Hashing()
	while(True):
		ans = int(input("Enter 1 for Insert, Enter 2 for Search, Enter 3 for Delete\n"))
		if ans == 1:
			lst = []
			n = int(input("Enter  number elememts: "))
			for i in range(0,n):
				ele = int(input())
				lst.append(ele)
			hh.insert(lst)
		elif ans == 2:
			item = int(input("Enter elememt to be searched "))
			result = hh.search(item)
			print(result)
		elif ans == 3:
			item = int(input("Enter elememt to be deleted "))
			hh.delete(item)
			
		else:
			quit()




if __name__ == "__main__":
	main()