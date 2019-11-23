# если число num должно быть кратно каждоу числу в диапазоне 2..9
cnt = 0

for num in range(2, 100):
	mod = 0
	for i in range(2, 10):
		mod += num % i

	if mod == 0:
		cnt += 1

print("количество кратных чисел: %d" % cnt)

cntArr = []
for i in range(2, 10):
	cntArr.append([i, 0])
for num in range(2, 100):
	for i in range(2, 10):
		if num % i == 0:
			cntArr[i-2][1] += 1

print("кратные числа: ", cntArr)