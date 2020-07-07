
hash_table = [None] * 13

class Addressing():
	def hash_calculator(self, num):
		return num % 13


	def insert(self, lst):
		for i in lst:
			mapping = self.hash_calculator(i)
			#print("mapping=", mapping)
			if hash_table[mapping] == None or hash_table[mapping] == "X":
				hash_table[mapping] = i
				#print("inserted ele")
			else:
				j = (mapping + 1) % 13
				while(j % 13 != mapping):
					print("j=", j)
					if hash_table[j] == None or hash_table[j] == "X":
						hash_table[j] = i
						break
					else:
						j = j + 1

	def delete(self, item):
		mapping = self.hash_calculator(item)
		#print("mapping", mapping)
		if hash_table[mapping] == item:
			#print("item=", item)	
			#hash_table.remove(item)
			hash_table[mapping] = "X"
		else:
			j = (mapping + 1) % 13
			while(j % 13 != mapping):
				#print("j=", j)
				if hash_table[j] == item:
					#hash_table.remove(item)
					hash_table[j] = 'X'
					break
				else:
					j = j + 1 

	def search(self, item):
		mapping = self.hash_calculator(item)
		if hash_table[mapping] == item:
			print("Elememt found at the index")
			return mapping
		else:
			j = (mapping + 1) % 13

			while(j % 13 != mapping):
				#print("J=", j)
				if hash_table[j%13] == item:
					print("Elememt found at the index")
					return j
					break
				else:
					j = j + 1
		return None




	
	def printtable(self):
		print(hash_table)
		#for i in hash_table:
		#	print("i=", i)


def main():
	hh = Addressing()
	while(True):
		ans = int(input("Enter 1 for Insert, Enter 2 for Search, Enter 3 for Delete\n"))
		if ans == 1:
			lst = []
			n = int(input("Enter  number elememts: "))
			for i in range(0,n):
				ele = int(input())
				lst.append(ele)
			hh.insert(lst)
			hh.printtable()
		elif ans == 2:
			item = int(input("Enter elememt to be searched "))
			result = hh.search(item)
			print(result)
			hh.printtable()
			
		elif ans == 3:
			item = int(input("Enter elememt to be deleted "))
			hh.delete(item)
			hh.printtable()

		else:
			quit()


if __name__ == "__main__":
	main()





