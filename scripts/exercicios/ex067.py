while True:
    print("-"*30)
    n = int(input("Quer ver a tabuada de qual valor? "))
    print("-"*30)
    if n < 0:
        break
    i = 1
    while True:
        print(f"{n} X {i} = {n*i}")
        i+=1
        if i > 10:
            break
print("Programa tabuada encerrado. Volte sempre!")
