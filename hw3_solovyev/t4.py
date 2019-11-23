import random

"""лень вбивать рандомный массив с клавиатуры, сделаю большой случайный список"""
def chkIfInList(list, val):
	for elem in list:
		if elem[0] == val:
			return list.index(elem)
	return -1

def getMaxVal(listIn):
	maxElem = listIn[0]
	for elem in listIn:
		if elem[1] >= maxElem[1]:
			maxElem = elem
	return listIn[listIn.index(maxElem)][0]

listOfInts = []
for i in range(100):
	listOfInts.append(random.randint(0, 100))
print("изначальный список: ", listOfInts)

listOfUnique = []
for number in listOfInts:
	idx = chkIfInList(listOfUnique, number)
	if idx == -1:
		listOfUnique.append([number, 1])
	else:
		listOfUnique[idx][1] +=1

print("список количества уникальных чисел в списке:")
print(listOfUnique)
print("==============================")
print("самое частое число: ", getMaxVal(listOfUnique))