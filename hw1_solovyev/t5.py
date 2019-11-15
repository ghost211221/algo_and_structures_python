print("введитедва символа")
n1 = input("первый символ: ")
n2 = input("вторый символ: ")

if 97 <= ord(n1) <= 122 and 97 <= ord(n2) <= 122:
    print("положение первой буквы: ", ord(n1) - 97 + 1)
    print("положение второй буквы: ", ord(n2) - 97 + 1)
    print("количество букв между введенными: ", end="")
    if ord(n2) > ord(n1):
        print(ord(n2) - ord(n1) - 1)
    elif ord(n1) > ord(n2):
        print(ord(n1) - ord(n2) - 1)
    else:
        print("символы равны, нет букв")
else:
    print("введите два символа")