def recReverseStr(num, revStr):
    if num == 0:
        print("через строку")
        print(revStr)
    else:
        digit = num % 10
        revStr += str(digit)
        recReverseStr(int(num / 10), revStr)

def recReverseInt(num, revNum):
    if num == 0:
        print("через число")
        print(revNum)
    else:
        digit = num % 10
        revNum = revNum * 10 + digit        
        recReverseInt(int(num / 10), revNum)

if __name__ == "__main__":
    try:
        num = int(input("введите натуральное число: "))
    except:
        print("не верный тип данных")
    if num >= 0:
        revStr = ""
        recReverseStr(num, revStr)
        revNum = 0
        recReverseInt(num, revNum)
    else:
        print("число олжно быть не отрицательным!")