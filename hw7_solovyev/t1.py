import random
import copy

def sortBuble(listIn):
	lists = copy.copy(listIn)
	for i in range(len(lists)):
		for j in range(len(lists) - i-1):
			if lists[j] > lists[j+1]:
				lists[j], lists[j+1] = lists[j+1], lists[j]
	return lists


def sortBubleM(listIn):
	lists = copy.copy(listIn)
	for i in range(len(lists)-1):
		# минус одна итерация
		for j in range(len(lists) - i-1):
			if lists[j] > lists[j+1]:
				lists[j], lists[j+1] = lists[j+1], lists[j]
	return lists

if __name__ == "__main__":
	listOfInts = []
	for i in range(100):
		listOfInts.append(random.randint(-100, 100))
	print("исходный массив:")
	print(listOfInts)

	print("сортировка пузырьком:")
	print(sortBuble(listOfInts))


	print("сортировка модифицированным пузырьком:")
	print(sortBubleM(listOfInts))


