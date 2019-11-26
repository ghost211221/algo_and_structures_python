import random
import timeit
import cProfile


"""возьмем скрипт для выбора максимального из минимальных элементов столбцов матрицы
    не будем печатать, дабы отключить влияние скорости вывода на замеры
    сложность = n**2 + n**2 + n + n + 1 + 1 + 1 + 10 + 10 = 2n**2 + 2n + 23
    (создание матриы, преобразование в список столбов, выбор минимума в стоблце, выбор максимума из минимумов, создание пустой матрицы, 
    создание пустого списка столбцов, создание списка минимумов, создание 10 строк матрицы, создание 10 столбцов)
    O(2n**2)
среднее время выполнения .0054
"""
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

def main():
    matrix = genMatrix()
    colsList = getColumns(matrix)
    minList = []
    for i in range(10):
        minList.append(getMinInList(colsList[i]))
    # print("максимальный элемент среди миниальных элементов столбцов: ", getMaxInList(minList))

def alternate():
    matrix = genMatrix()
    minColElem2 = None
    for i in range(10):
        minColElem1 = matrix[0][i]
        for j in range(10):
            if matrix[j][i] < minColElem1:
                minColElem1 = matrix[j][i]
                if not minColElem2:
                    minColElem2 = minColElem1
                elif minColElem2 < minColElem1:
                    minColElem2 = minColElem1
    # print("максимальный элемент среди миниальных элементов столбцов: ", minColElem2)



if __name__ == "__main__":
    print("начальная реализация")
    print(timeit.timeit("main()", setup="from __main__ import main", number=10000))
    cProfile.run('main()')
    print("=============================================")
    print("альтернативня реализация")
    print(timeit.timeit("alternate()", setup="from __main__ import alternate", number=10000))
    cProfile.run('alternate()')
"""результаты
начальная реализация
1.0378651450000689
         781 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
      100    0.000    0.000    0.000    0.000 random.py:173(randrange)
      100    0.000    0.000    0.000    0.000 random.py:217(randint)
      100    0.000    0.000    0.000    0.000 random.py:223(_randbelow)
       10    0.000    0.000    0.000    0.000 t1.py:14(genMAtrixRow)
        1    0.000    0.000    0.000    0.000 t1.py:20(genMatrix)
        1    0.000    0.000    0.000    0.000 t1.py:26(getColumns)
       10    0.000    0.000    0.000    0.000 t1.py:35(getMinInList)
        1    0.000    0.000    0.000    0.000 t1.py:49(main)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      230    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      125    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


=============================================
альтернативня реализация
0.9318905209997865
         648 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
      100    0.000    0.000    0.000    0.000 random.py:173(randrange)
      100    0.000    0.000    0.000    0.000 random.py:217(randint)
      100    0.000    0.000    0.000    0.000 random.py:223(_randbelow)
       10    0.000    0.000    0.000    0.000 t1.py:14(genMAtrixRow)
        1    0.000    0.000    0.000    0.000 t1.py:20(genMatrix)
        1    0.000    0.000    0.000    0.000 t1.py:57(alternate)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      110    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
      100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
      123    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
"""
    

    

## получился интересный результат:
## во втором варианте меньше вызовов функций, но делается дольше при малых значениях numer, порядка 100
## если сделать 1000 и выше второй вариант становится быстрее
## другой идеи как ускорить, не используя втроенные функции, у меня пока нет