import random

from memory_profiler import profile

def genMAtrixRow():
    listOfInts = []
    for i in range(1000):
        listOfInts.append(random.randint(0, 1000))
    return listOfInts

def genMatrix():
	matrix = []
	for i in range(1000):
		matrix.append(genMAtrixRow())
	return matrix

def getColumns(matrix):
    colsList = []
    for i in range(1000):
        col = []
        for j in range(1000):
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

@profile
def main():
    matrix = genMatrix()
    colsList = getColumns(matrix)
    minList = []
    for i in range(1000):
        minList.append(getMinInList(colsList[i]))
    # print("максимальный элемент среди миниальных элементов столбцов: ", getMaxInList(minList))

@profile
def alternate():
    matrix = genMatrix()
    minColElem2 = None
    for i in range(100):
        minColElem1 = matrix[0][i]
        for j in range(1000):
            if matrix[j][i] < minColElem1:
                minColElem1 = matrix[j][i]
                if not minColElem2:
                    minColElem2 = minColElem1
                elif minColElem2 < minColElem1:
                    minColElem2 = minColElem1
    # print("максимальный элемент среди миниальных элементов столбцов: ", minColElem2)



if __name__ == "__main__":

    main()

    alternate()
