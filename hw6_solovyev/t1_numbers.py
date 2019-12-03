"""для разбора возьму решето Эратосфена и программу с матрицами, 
благо у каждой программы два варианта кода есть

по параметрам системы:
Ubuntu 18.04 x86_64 5.0.0-36-generic
Python 3.6.9, но есть еще 3.8, но не основной


"""
from memory_profiler import profile

@profile
def simpleGet(num):
	lst = []
	k = 0
	digit = 2
	while len(lst) < num:
		for i in range(2, digit):
			if digit % i == 0:
				break
		else:
			lst.append(digit)
		digit += 1
	return lst[-1]

@profile
def eratosfen(num):
	lst = []
	tempArr = list(range(num*10))
	tempArr[1] = 0
	digit = 2
	while len(lst) < num:
		if tempArr[digit] != 0:
			lst.append(tempArr[digit])
			for j in range(digit, num*10, digit):
				tempArr[j] = 0
		digit += 1
	return lst[-1]

if __name__ == "__main__":
	n = 500
	nonEratosfenRes = simpleGet(n)	
	print("простой поиск: ", nonEratosfenRes)
	eratosfenRes = eratosfen(n)	
	print("решето Эратосфена: ",eratosfenRes)