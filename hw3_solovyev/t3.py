import random

def getIdxOfMin(listIn):
	minNum = listIn[0]
	for elem in listIn:
		if elem <= minNum:
			minNum = elem
	return listIn.index(minNum)

def getIdxOfMax(listIn):
	maxNum = listIn[0]
	for elem in listIn:
		if elem >= maxNum:
			maxNum = elem
	return listIn.index(maxNum)

listOfInts = []
for i in range(10):
	listOfInts.append(random.randint(0, 100))
print("изначальный список: ", listOfInts)

idxOfMax = getIdxOfMax(listOfInts)
idxOfMin = getIdxOfMin(listOfInts)

listOfInts[idxOfMax], listOfInts[idxOfMin] = listOfInts[idxOfMin], listOfInts[idxOfMax]
print("результирующий список: ", listOfInts)