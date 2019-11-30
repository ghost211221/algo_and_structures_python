"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import namedtuple

def convertToListOfInt(strIn):    
    arr = list(strIn)
    list2ret = []
    for item in arr:
        try:
            list2ret.append(int(item))
        except:
            if 65 <= ord(item) <= 70:
                list2ret.append(10 + ord(item) - 65)
            elif 97 <= ord(item) <= 102:
                list2ret.append(10 + ord(item) - 97)
            else:
                print("не верный ввод")
                sys.exit(1)
    return list2ret

def addZeros(list1, list2):
    while len(list1) < len(list2):
        list1.append(0)

def convertToHex(val):
    if val >= 10:
        return(chr(val-10+65))
    else:
        return str(val)

def convertTupListToListOfValues(tupList):
    list2ret = []
    for item in tupList:
        print(item)
        list2ret.append(convertToHex(item[0]))
    list2ret.reverse()
    return list2ret

def sum(list1, list2):
    list1.reverse()
    list2.reverse()

    if len(list1) < len(list2):
        addZeros(list1, list2)
    elif len(list1) > len(list2):
        addZeros(list2, list1)
    bit = namedtuple("bit", ["value", "carryOut"])
    tupList = []
    for i in range(len(list1)):
        value = 0
        carryOut = 0
        if i > 0:
            value = (list1[i] + list2[i] + tupList[i-1][1]) % 16
            carryOut = (list1[i] + list2[i] + tupList[i-1][1]) // 16            
        else:
            value = (list1[i] + list2[i]) % 16
            carryOut = (list1[i] + list2[i]) // 16 
        bitTup = bit(value=value, carryOut=carryOut)    
        tupList.append(bitTup)
    return convertTupListToListOfValues(tupList)

def mult(val1, val2):
    """ не хватает времени что по-правильному, построить алгоритм аналогичный умножению столбиком.
        поэтому сделаю преобразование hex -> dec, mult, dec -> hex
    """
    vall1 = int(val1, 16)
    vall2 = int(val2, 16)
    print(vall1, vall2)


    return list('{:x}'.format(vall1*vall2))




if __name__ == "__main__":
    val1 = input("введите первое число: ")
    list1 =  convertToListOfInt(val1)
    val2 = input("введите первое число: ")
    list2 =  convertToListOfInt(val2)

    print("сумма: ", sum(list1, list2))
    print("умножение: ", mult(val1, val2))
