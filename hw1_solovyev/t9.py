print("Введите три числа:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a < b < c:
    print(b)
elif c < b < b:
    print(b)
elif b < a < c:
    print(a)
elif c < a < b:
    print(a)
elif b < c < a:
    print(c)
elif a < c < b:
    print(c)
else:
    print("минимум числа равны")