import sys

def getSumOfElems(listIn):
	sum = 0
	for elem in listIn:
		sum += elem

	return sum

def inputRow(strName):
	try:
		rowList = list(map(int, input("введите %s строку матрицы: " % strName).split(" ")))
	except:
		print("не верный тип")
		sys.exit(1)

	if len(rowList) != 4:
		print("не верная длина строки")
		sys.exit(1)
	return rowList

matrix = []
matrix.append(inputRow("первую"))
matrix.append(inputRow("вторую"))
matrix.append(inputRow("третью"))
matrix.append(inputRow("четвертую"))

for row in matrix:
	row.append(getSumOfElems(row))

print("результат:")
for row in matrix:
	print(row)