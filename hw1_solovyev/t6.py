sym = int(input("введите символ: "))

if 1 <= sym <= 26:
    print("выбрана буква: ", chr(sym))
else:
    print("не верный символ")