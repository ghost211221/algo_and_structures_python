import sys


def recCalc(): 
    stop = False
    try:
        num1 = int(input("введите первое число: "))
        num2 = int(input("введите второе число: "))
        try:
            op = input("введите знак операции или 0 для выхода: ")
            if op == "0":
                stop = True
                print("выход") 
                sys.exit()               
            elif op == "+":
                print(num1 + num2)
            elif op == "-":
                print(num1 - num2)
            elif op == "*":
                print(num1 * num2)
            elif op == "/":
                if num2 == 0:
                    print("деление на 0!")
                else:
                    print(num1 / num2)
            else:
                raise Exception
            print("==========================")
        except:        
            if stop:                
                sys.exit(1)    
            print("не верная операция")
    except:
        if stop:                
            sys.exit(1)
        print("не верный тип данных")
    recCalc()

if __name__ == "__main__":
    recCalc()