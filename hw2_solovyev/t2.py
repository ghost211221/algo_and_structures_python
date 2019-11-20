def recNum(num, even, odd):
    if num == 0:
        print("odd: ", odd, "even: ", even)
    else:
        digit = num % 10
        if digit % 2 == 0:
            even += 1
        else:
            odd += 1
        recNum(int(num / 10), even, odd)

if __name__ == "__main__":
    try:
        num = int(input("введите натуральное число: "))
    except:
        print("не верный тип данных")
    if num >= 0:
        even = 0
        odd  = 0
        recNum(num, even, odd)
    else:
        print("число олжно быть не отрицательным!")