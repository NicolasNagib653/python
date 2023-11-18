times = [1,2,3,4]

for i in range(1,4):
    times[i] = input("Nome do {}o. time: " .format(i))

for i in range(1,4):
    for j in range(i,4):
        if i != j:
            print("{}       [] x [] {}" .format(times[i],times[j]))

