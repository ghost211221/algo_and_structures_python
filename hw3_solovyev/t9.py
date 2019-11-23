import random

"""сгенерю матрицу динамически 10х10"""

def genMAtrixRow():
    listOfInts = []
    for i in range(10):
        listOfInts.append(random.randint(0, 100))
    return listOfInts

def genMatrix():
	matrix = []
	for i in range(10):
		matrix.append(genMAtrixRow())
	return matrix

def getColumns(matrix):
    colsList = []
    for i in range(10):
        col = []
        for j in range(10):
            col.append(matrix[j][i])
        colsList.append(col)
    return colsList

def getMinInList(listIn):
    minElem = listIn[0]
    for elem in listIn:
        if elem < minElem:
            minElem = elem
    return minElem

def getMaxInList(listIn):
    maxElem = listIn[0]
    for elem in listIn:
        if elem > maxElem:
            maxElem = elem
    return maxElem

if __name__ == "__main__":
    matrix = genMatrix()
    print("матрица:")
    for i in range(10):
        print(matrix[i])

    colsList = getColumns(matrix)
    print("столбцы:")
    for i in range(10):
        print(colsList[i])
    minList = []
    for i in range(10):
        minList.append(getMinInList(colsList[i]))
    print("максимальный элемент среди миниальных элементов столбцов: ", getMaxInList(minList))

