number = int(input("введите трехзначное число: "))

if 100 <= number < 1000:
    units = number % 10;
    decs  = int(number % 100 / 10)
    hundr = int(number / 100)
    summ  = units + decs + hundr
    mult  = units * decs * hundr
    print("сумма: ", summ)
    print("произведение: ", mult)
else:
    print("не правильное число")
