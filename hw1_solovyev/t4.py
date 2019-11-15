import random

print("введите границы для целого числа")
n1 = int(input("первая граница: "))
n2 = int(input("вторая граница: "))
if n2 > n1:
    print(random.randint(n1, n2))
elif n1 > n2:
    print(random.randint(n2, n1))
else:
    print("числа равны")
################################################
print("введите границы для дробного числа")
n1 = float(input("первая граница: "))
n2 = float(input("вторая граница: "))
if n2 > n1:
    print(random.uniform(n1, n2))
elif n1 > n2:
    print(random.uniform(n2, n1))
else:
    print("числа равны")
################################################
print("введите границы для символа")
n1 = input("первая граница: ")
n2 = input("вторая граница: ")

if 97 <= ord(n1) <= 122 and 97 <= ord(n2) <= 122:
    if ord(n2) > ord(n1):
        print(chr(random.randint(ord(n1), ord(n2))))
    elif ord(n1) > ord(n2):
        print(chr(random.randint(ord(n2), ord(n1))))
    else:
        print("символы равны")
else:
    print("введите два символа")