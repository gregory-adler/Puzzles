import itertools

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
		#print ("index", index)
		if index not in p:
			p[index] = 1
			#print ("new")
		else:
			#print ("additional")
			p[index] +=1
			#print ("math")
			#print ((p[index]/2))
			if ((p[index] % 2) == 0):
				pairs +=1

	return pairs


def jumpingOnClouds(c): 
    counter = 0
    switch = False
    for i in range (0, (len (c)-1)):
        #print ("i", i)
        if (switch):
            switch = False
           # print ("continuing")
            continue
        if len(c) > i+2 and c[i+2] == 0:
            #print ("skip two")
            switch = True
        else:
        	continue
           # print ("skip one")
        #print ("step")
        counter +=1

    return counter



def repeatedString(s, n):
	if (s== 'a'):
		return n
	istring = ''
	multiplier = int(n/(len(s))) +1
	array = []
	# print (multiplier)
	counter =0

	for i in range (0, multiplier):
		array.append(s)

	istring = istring.join(array)
	# print (len(istring))
	while (len(istring) > n):
		istring = istring[:-1]
	# print (istring)

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

	return newArrayj

def hashOfHash(magazine, note):
	hashTable = {}
	answer = "Yes"
	
	for i in magazine:
		if i in hashTable:
			hashTable[i]+=1
		else:
			hashTable[i] = 1

	for j in note:
		if j in hashTable:
			if hashTable[j]>0:
				hashTable[j]-=1
			else:
				answer = "No"
		else: 
			answer = "No"

	print (answer)

def twoStrings(s1, s2):
	for j in s1:
		if j in s2:
			return "YES"

	return ("NO")


def makeAnagram(a, b):
	dict1 = {}
	dict2 = {}
	counter = 0
	deleteKeys = []

	for item in a:
		if item in dict1:
			dict1[item]+=1
		else:
			dict1[item] =1

	for item in b:
		if item in dict2:
			dict2[item]+=1
		else:
			dict2[item] = 1


	print ("dict1: ", dict1)
	print ("dict2:" , dict2)


	print ("loop")
	for key in dict1.keys():
		print ("key", key)
		if key in dict2:
			print ("same")
			if dict1[key] == dict2[key]:
				print ("match")
				continue
			elif dict1[key] > dict2[key]:
				while dict1[key] > dict2[key]:
					print ("minus one")
					dict1[key]-=1
					counter +=1
		else:
			print ("no match")
			counter +=dict1[key]
			deleteKeys.append(key)

	for key in deleteKeys:
		del (dict1[key])
		deleteKeys = []

	print ("loop 2")
	for key in dict2.keys():
		print ("key", key)
		if key in dict1:
			print ("same")
			if dict1[key] == dict2[key]:
				print ("match")
				continue
			elif dict2[key] > dict1[key]:
				while dict2[key] > dict1[key]:
					print ("minus one")
					dict2[key]-=1
					counter +=1
		else:
			print ("no match")
			counter +=dict2[key]
			deleteKeys.append(key)

	for key in deleteKeys:
		del (dict2[key])

	return counter

def hourglassSum(arr):
	localSum = 0
	maxSum = -50
	for i in range (0, len(arr)):
		print (arr[i])
		for j in range (0, len(arr[i])):
			if (i+2 <len(arr) and j+2 < len(arr[i])):
				print ("hourglass")
				print (arr[i][j], arr[i][j+1], arr[i][j+2],arr[i+1][j] ,arr[i+2][j+1] ,arr[i+2][j+1] ,arr[i+2][j+2])
				localSum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
				print ("localSum", localSum)
				if localSum > maxSum:
				    maxSum = localSum
				    localSum = 0
				else: 
					print ("next")
	return maxSum


def countSwaps(a):
	counter =0
	status = True

	while (status):
		temp = 0
		for i in range (0, len(a)-1):
			#print ("array:", a)
			#print (a[i])
			# swap
			if (a[i+1] < a[i]):
				#print ("swap")
				a[i+1], a[i] = a[i], a[i+1]
				counter +=1
				temp +=1
		if (temp ==0):
			#print ("done")
			status = False

	print ("Array is sorted in", counter, "swaps.")
	print ("First Element:", a[0])
	print ("Last Element:", a[-1])


def alternatingCharacters(s):
	print (s)
	boolean = True
	counter =0
	i = 0
	while (boolean):
		if len(s) > i+1:
			if s[i] == s[i+1]:
				counter+=1
				i+=1
			#two fine
			else:
				i+=1
		#done iterating
		else:
			boolean =False
	return counter


def whatFlavors(cost, money):
	solutions = {}
	for i in range (0, len(cost)):
		compliment = money - cost[i]
		if (compliment == cost[i]):
			#print ("same compliment", compliment)
			for j in range (i+1, len(cost)):
				if cost[j] == cost[i]:
					#print ("solution")
					print (i+1, j+1)
					return
		else: 
			solutions[compliment] = i

	for i in range (0, len(cost)):
		if cost[i] in solutions:
			print (i+1, (solutions[cost[i]]+1))
	return


def primality(n):
    if (n==1):
        return "Not prime"
    for i in range (2, n):
        if (n % i ==0):
            return "Not prime"
        if (i>1001):
            return "Prime"
    
    return "Prime"


def maxSubsetSum(arr):
	maxSum = 0
	bestSolution = [None] * len(arr)
	# print (bestSolution)

	for i in range (0, len(arr)):
		if (i >= 3 and bestSolution[i-2]!= None and bestSolution[i-3]!= None):
			bestSolution[i] = max(bestSolution[i-2], bestSolution[i-3]) + max(0, arr[i])
		elif (i >= 2 and bestSolution[i-2]!= None):
			#print ("iterating solution")
			#print (bestSolution[i-2])
			bestSolution[i] =bestSolution[i-2] + max(0, arr[i])
		else:
			bestSolution[i] = max(0, arr[i])

	# print (bestSolution)

	for item in bestSolution:
		if item > maxSum:
			maxSum = item

	return maxSum

def height(root):
    if root == None:
        return -1
    else:
        return 1 + max(height(root.left), height(root.right))



def minimumAbsoluteDifference(arr):
	sortedArr = sorted(arr)
	answer = abs(sortedArr[-1] - sortedArr[0])
	print (sortedArr)
	for i in range (0, len(arr)-1):
		difference = abs(sortedArr[i+1] - sortedArr[i])
	if difference < answer:
	    answer = difference
	return answer


def luckBalance(k, contests):
	answer =0
	important = []

	for item in contests:
		if item[1] == 0:
			answer+= item[0]
		else:
			important.append(item[0])
			important = sorted (important, reverse = True)


	for i in range (0, len(important)):
		if i < k:
			answer += important[i]
		else:
			answer -= important[i]

	return answer

def fibonacci(n):
	if (n == 0):
		return 0
	if (n ==1):
		return 1
	return fibonacci(n-1) + fibonacci (n-2)	

def getCombinations(list, n):
	for i in range (0, len(list)+1):
		for item in (itertools.combinations(list,i)):
			print (item)

def stepPerms(n):
	count = recursion(0, n)
	return count


def recursion(height,n):
	if height == n:
		return 1
	elif height > n:
		return 0
	else:
		return recursion(height +1 ,n) + recursion(height +2 ,n) + recursion(height+3,n)


c =(0,0,0,0,1,0)
print jumpingOnClouds(c)

stuff = [1,2,3,4,5]

stuff.append(6)

print stuff