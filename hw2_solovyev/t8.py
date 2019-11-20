import copy

def calcInNumber(num, digit):
    numInt = copy.deepcopy(num)
    cnt = 0
    while numInt > 0:
        if numInt % 10 == digit:
            cnt += 1
        numInt = int(numInt / 10)
    return cnt
        

if __name__ == "__main__":
    n = 0
    while n <= 0:
        try:
            n = int(input("введите количество элементов: "))
        except:
            print("не верный тип данных")
    digit = 0
    while digit <= 0:
        try:
            digit = int(input("введите цифру для поиска: "))
        except:
            print("не верный тип данных")
    cnt = 0
    while n > 0:
        num = 0
        while num <= 0:
            try:
                num = int(input("введите число последовательности: "))
            except:
                print("не верный тип данных")
        cnt += calcInNumber(num, digit)
        n -= 1

    print("цифра %d встретилась %d раз" % (digit, cnt))
            