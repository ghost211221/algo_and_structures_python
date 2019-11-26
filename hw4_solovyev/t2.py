import timeit
import cProfile

"""
замерял при number=100 и искал 1000е число
больших значений не ставил, ждать долго
простой способ
22.401774850999573
         8923 function calls in 0.226 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.226    0.226 <string>:1(<module>)
        1    0.225    0.225    0.226    0.226 t2.py:38(simpleGet)
        1    0.000    0.000    0.226    0.226 {built-in method builtins.exec}
     7919    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


=============================================
решето Эратосфена
0.23518985099963174
         8923 function calls in 0.004 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
        1    0.003    0.003    0.004    0.004 t2.py:51(eratosfen)
        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
     7919    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

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
	n = 1000
	nonEratosfenRes = simpleGet(n)	
	print("простой поиск: ", nonEratosfenRes)
	eratosfenRes = eratosfen(n)	
	print("решето Эратосфена: ",eratosfenRes)
	print("=========================================")
	print("Замеры")
	print()
	print("простой способ")
	print(timeit.timeit("simpleGet(n)", setup="from __main__ import simpleGet, n", number=100))
	cProfile.run('simpleGet(n)')
	print("=============================================")
	print("решето Эратосфена")
	print(timeit.timeit("eratosfen(n)", setup="from __main__ import eratosfen, n", number=100))
	cProfile.run('eratosfen(n)')
