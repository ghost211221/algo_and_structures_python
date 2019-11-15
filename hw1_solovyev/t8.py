print("Введите год:")
year = int(input("a = "))

if (year % 4 > 0) or (year % 100 == 0) and (year % 400 > 0):
    print("год обычный")
else:
    print("год високосный")