def countingValleys(n, s):

	n = len(s)
	count = 0
	valley = 0
	for i in range (0, n):
		if s[i] == 'U':
	 	 	count+=1
	 	elif s[i]=='D':
	 	 	count-=1 
	 	 	if count ==-1:
	 	 		valley +=1

	return valley

	# print "count: " + str(count)

	# print "valley: "+ str(valley)


def sockMerchant(n, ar):

 	pairs = 0 
 	p = {}
 	index = 0 

	for i in range (0, len(ar)):
		index = ar[i]
		print ("index", index)
		if index not in p:
			p[index] = 1
			print ("new")
		else:
			print ("additional")
			p[index] +=1
			print ("math")
			print ((p[index]/2))
			if ((p[index] % 2) == 0):
				pairs +=1

	return pairs


def jumpingOnClouds(c): 
    counter = 0
    switch = False
    for i in range (0, (len (c)-1)):
        print ("i", i)
        if (switch):
            switch = False
            print ("continuing")
            continue
        if len(c) > i+2 and c[i+2] == 0:
            print ("skip two")
            switch = True
        else:
            print ("skip one")
        print ("step")
        counter +=1

    return counter



def repeatedString(s, n):
	if (s== 'a'):
		return n
	istring = ''
	multiplier = int(n/(len(s))) +1
	array = []
	print (multiplier)
	counter =0

	for i in range (0, multiplier):
		array.append(s)

	istring = istring.join(array)
	print (len(istring))
	while (len(istring) > n):
		istring = istring[:-1]
	print (istring)

	for letter in istring:
		if letter == 'a':
			counter+=1

	return counter

def rotateArrayLeft(a,d):
	newArray = [-1] * len(a)
	difference = 0
	for i in range (0, len(a)):
		difference = i-d
	if difference <0:
		index = difference + len(a)
		print ("index", index)
		newArray[index] = a[i]
	else:
		newArray[difference] = a[i]

	return newArray

c =(0,0,0,0,1,0)
print jumpingOnClouds(c)