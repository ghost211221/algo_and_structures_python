"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""
from collections import namedtuple
import sys

def getInput(text, typeDef):
    try:
        return typeDef(input(text))
    except:
        print("не верный тип: ", inVal)
        sys.exit(1)

def convertType(inVal, typeDef):
    try:
        return typeDef(inVal)
    except:
        print("не верный тип: ", inVal)
        sys.exit(1)

def parseStrToFirmInfo(strIn):
    arr = strIn.split(" ")
    if len(arr) != 5:
        print("не верный ввод")
        print(len(arr), arr)
        sys.exit(1)
    compName = arr[0]
    quad1 = convertType( arr[1], int)
    quad2 = convertType( arr[2], int)
    quad3 = convertType( arr[3], int)
    quad4 = convertType( arr[4], int)

    return compName, quad1, quad2, quad3, quad4

def calcCompMean(listIn):
    """расчет среднего дохода для отдельной компании"""
    summ = 0.0
    for item in listIn:
        summ += item
    return summ / len(listIn)

def calcMean(tupList):
    """расчет среднего дохода всех компаний"""
    summ = 0.0
    for item in tupList:
        summ += item[5]
    return summ / len(tupList)

def printWinners(tupList, mean):
    print("список компаний с прибылью больше средней")
    for item in tupList:
        if item[5] >= mean:
            print(item)

def printLoosers(tupList, mean):
    print("список компаний с прибылью меньше средней")
    for item in tupList:
        if item[5] < mean:
            print(item)


if __name__ == "__main__":
    numberOfFirms = getInput("введте количество фирм: ", int)
    compTup = namedtuple("compTup", ["compName", "quad1", "quad2", "quad3", "quad4", "mean"])
    compList = []
    for i in range(1, numberOfFirms+1):
        compStr = getInput("введте информацию о фирме в формате (название доход за 1 квартал доход за 2 квартал доход за 3 квартал доход за 4 квартал): ", str)
        compParList = list(parseStrToFirmInfo(compStr))
        tup = compTup(compName=compParList[0], quad1=compParList[1], quad2=compParList[2], quad3=compParList[3], quad4=compParList[4], mean=calcCompMean(compParList[1:4]))
        compList.append(tup)
    fullMean = calcMean(compList)
    printWinners(compList, fullMean)
    printLoosers(compList, fullMean)

