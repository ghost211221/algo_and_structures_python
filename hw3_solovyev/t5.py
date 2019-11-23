import random

def getIdxOfMaxNegAbs(listIn):
	maxNum = listIn[0]
	for elem in listIn:
		if (elem < 0) and (abs(elem) >= abs(maxNum)):
			maxNum = elem
	return maxNum, listIn.index(maxNum)

def getIdxOfMaxNeg(listIn):
	for elem in listIn:
		if elem < 0:
			maxNum = elem
	for elem in listIn:
		if (elem < 0) and (maxNum < 0) and (elem >= maxNum):
			maxNum = elem
	return maxNum, listIn.index(maxNum)

listOfInts = []
for i in range(100):
	listOfInts.append(random.randint(-100, 100))
print("изначальный список: ", listOfInts)

print("максимальное по модулю отрицательное число: ", getIdxOfMaxNegAbs(listOfInts))
print("максимальное  отрицательное число: ", getIdxOfMaxNeg(listOfInts))