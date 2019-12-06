import random
import copy

def sortMerge(listIn):
	lists = copy.copy(list(listIn))
	if len(lists) > 1:
		print(len(lists), type(lists))
		mid = len(lists) // 2
		left = lists[:mid]
		right = lists[mid:]

		sortMerge(left)
		sortMerge(right)

		i = 0
		j = 0
		k = 0
		while i < len(left) and j < len(right):
			if left[i] < right[i]:
				lists[k] = left[i]
				i += 1
			else:
				lists = right[j]
				j += 1
			k += 1

		while i < len(left):
			print(k)
			print(lists)
			lists[k] = left[i]
			i += 1
			k += 1

		while j < len(right):
			lists[k] = right[j]
			j += 1
			k += 1
	return lists

if __name__ == "__main__":
	listOfFloats = []
	for i in range(100):
		listOfFloats.append(random.uniform(0, 50))
	print("исходный массив:")
	print(listOfFloats)

	print("сортировка пузырьком:")
	print(sortMerge(listOfFloats))