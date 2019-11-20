def printASCII():
    cnt = 0
    for i in range(32, 128):
        print(i, chr(i), end="")
        if cnt == 9:
            print()
            cnt = 0
        else:
            print(" ", end="")
            cnt += 1

if __name__ == "__main__":
    printASCII()