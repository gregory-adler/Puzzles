
def hashNumber(string):
	a=  str(abs(hash(string)))
	return int(a[-4:])


def main():
	a= ["seven", 710]
	b= ["two", 210]
	array = [None] * 9999

	add(array, a)
	add(array, b)

	delete(array, a)


	for i in range(0, len(array)):
		if array[i] == None:
			continue
		else:
			print "index", i 
			print "value", array[i]

def add(array, item):
	key = item[0]
	value = item[1]

	index = hashNumber(key)
	array[index] = value


def delete(array,item):
	key = item[0]
	value = item[1]
	index = hashNumber(key)
	array[index] = None

main()