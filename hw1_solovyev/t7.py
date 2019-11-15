print("Введите длины сторон предполагаемого треугольника:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
 
if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
    if a == b == c:
        print("треугольник равносторонний")
    elif a == b or a == c or b == c:
        print("треугольник равнобедренный")
    else:
        print("треугольник разносторонний")
else:
    print("Треугольник не существует")