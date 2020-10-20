

class MyStack:
	contador = 0
	def __init__ (self, list):
		self.data = list
	def pop():
		self.data = self.data[:-1]
		self.contador-= 1
	def push(ele):
		self.data.append(ele)
		self.contador+= 1
	def top():
		length = len(self.data) -1
		return self.data[len]
	def isEmpty():
		return self.contador <= 0
	def find(element):
		isExist = Flase
		for x in self.data:
			isExist = isExist  | ( x == element)
		
		return isExist
		
