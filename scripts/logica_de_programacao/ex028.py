r = "1"
while r != "3":
    print("=====================")
    print("|      M E N U      |")
    print("=====================")
    print("|   [1] de 1 a 10   |")
    print("|   [2] de 10 a 1   |")
    print("|   [3] sair        |")
    print("=====================")

    r = input("")
    if r == "1":
        i = 0
        while i <= 10:
            print(i)
            i = i + 1
    elif r == "2":
        i = 10
        while i >= 0:
            print(i)
            i = i - 1