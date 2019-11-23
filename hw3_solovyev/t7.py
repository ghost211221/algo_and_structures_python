import random

def getIdxOfMin1(listIn):
	minNum = listIn[0]
	for elem in listIn:
		if elem < minNum:
			minNum = elem
	return listIn.index(minNum)

def getIdxOfMin2(listIn, idx1):
	minNum = listIn[0]
	for elem in listIn:
		if (elem < minNum) & (listIn.index(elem) != idx1):
			minNum = elem
	return listIn.index(minNum)

listOfInts = []
for i in range(10):
	listOfInts.append(random.randint(0, 100))
print("изначальный список: ", listOfInts)

idxOfMin1 = getIdxOfMin1(listOfInts)
idxOfMin2 = getIdxOfMin2(listOfInts, idxOfMin1)

print(idxOfMin1, listOfInts[idxOfMin1])
print(idxOfMin2, listOfInts[idxOfMin2])