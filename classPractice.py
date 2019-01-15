class Node(object):


	def __init__(self, name, age):
		self.name = name
		self.age = age

	def test (self):
		print ("hello world")

	def printSelf (self):
		print ("Name: ", name)
		print ("Age: ", age)




name = raw_input("Please enter your name: ")
age = raw_input("Please enter your age: ")
Test =  Node(name,age)
Test.test()
Test.printSelf()