x1 = float(input("введите x1: "))
y1 = float(input("введите y1: "))
x2 = float(input("введите x2: "))
y2 = float(input("введите y2: "))


# после пары математических операций:
k = (y2 - y1) / (x2 - x1)
b = y1 - k * x1

# пишем уравнение
print("y=%.2f*x" % k, end='')
if b < 0:
    print("-%.2f" % b)
else:
    print("+%.2f" % b)

# для проверки вычисляем y1 и y2 от введенных x1 и x2
print("x1->", (k*x1+b))
print("x2->", (k*x2+b))