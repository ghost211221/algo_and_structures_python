if __name__ == "__main__":
    try:
        n = int(input("введите количество элементов: "))
    except:
        print("не верный тип данных")
    if n >= 1:
        sumSeq = 0
        for i in range(1, n+1):
            sumSeq += i
        sumForm = n * (n + 1) / 2
        if sumSeq == sumForm:
            print("все верно")
        else:
            print("не верно!")
    else:
        print("число олжно быть не отрицательным!")