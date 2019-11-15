num1 = 5
num2 = 6

bit_and = num1 & num2
bit_or  = num1 | num2
bit_xor = num1 ^ num2
shiftL  = num1<<2
shiftR  = num1>>2

print("побитовое И: ", bit_and, bin(bit_and))
print("побитовое ИЛИ: ", bit_or, bin(bit_or))
print("побитовое исключающее ИЛИ: ", bit_xor, bin(bit_xor))
print("сдвиг влево: ", shiftL, bin(shiftL))
print("сдвиг вправо: ", shiftR, bin(shiftR))

"""
сдвиг влево на один разряд эквивалентен умножению на 2,
аналогично на два разряда -> умножение на 4
соответственно, сдвиг впраыо на один разряд эквивалентен делению на 2
нацело, аналогично на два разряда -> деление на 4
"""