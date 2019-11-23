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

def getSumOfElems(listIn, idxStart, idxStop):
	sum = 0
	for idx in range(idxStart, idxStop+1):
		sum += listIn[idx]

	return sum

listOfInts = []
for i in range(10):
	listOfInts.append(random.randint(0, 100))
print("изначальный список: ", listOfInts)

idxOfMax = getIdxOfMax(listOfInts)
idxOfMin = getIdxOfMin(listOfInts)

sum = 0
if (idxOfMax >= idxOfMin + 2):
	# иначе нет смысла
	sum = getSumOfElems(listOfInts, idxOfMin+1, idxOfMax-1)
elif (idxOfMin >= idxOfMax + 2):
	sum = getSumOfElems(listOfInts, idxOfMax+1, idxOfMin-1)
print("сумма: ", sum)