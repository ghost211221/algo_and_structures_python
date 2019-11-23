list1 = list(map(int, input("введите массив: ").split(" ")))
list2 = []
for number in list1:
	if number % 2 == 0:
		list2.append(list1.index(number))

print("список индексов четных элементов:")
print(list2)