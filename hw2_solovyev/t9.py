import copy

def calcDigSum(num):
    numInt = copy.deepcopy(num)
    digSum = 0
    while numInt > 0:
        digSum = numInt % 10
        numInt = int(numInt / 10)
    return digSum
        

if __name__ == "__main__":
    n = 0
    while n <= 0:
        try:
            n = int(input("введите количество элементов: "))
        except:
            print("не верный тип данных")
    number = 0
    digSum = 0
    while n > 0:
        num = 0
        while num <= 0:
            try:
                num = int(input("введите число последовательности: "))
            except:
                print("не верный тип данных")
        tempSum = calcDigSum(num)
        if tempSum > digSum:
            digSum = tempSum
            number = num
        n -= 1

    print("число %d сумма %d" % (number, digSum))
            