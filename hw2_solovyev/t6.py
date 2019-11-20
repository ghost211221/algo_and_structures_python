import random

def recGuess(tryCnt, num):
    if tryCnt == 9:
        print("Игра закончена, загаданное число: ", num)
    elif tryCnt == -1:
        print("вы угадали")
    else:
        try:
            ans = int(input("ваш ответ: "))
            if ans < 0:
                raise Exception
            else:
                if ans < num:
                    print("мало")
                elif ans > num:
                    print("много")
                else:
                    tryCnt = -2
                
                tryCnt += 1
        except:
            # print("не верный ввод")
            pass
        print("========================")
        recGuess(tryCnt, num)

if __name__ == "__main__":
    tryCnt = 0
    num = random.randint(0, 100)
    recGuess(tryCnt, num)