lugar = [1,2,3,4,5,6,7,8,9,10]
resp = "s"
i = 0
 
def lugares():
    print("[ B{} ][ B{} ][ B{} ][ B{} ][ B{} ][ B{} ][ B{} ][ B{} ][ B{} ][ B{} ]".format(lugar[0], lugar[1], lugar[2], lugar[3], lugar[4], lugar[5], lugar[6], lugar[7], lugar[8], lugar[9]))

lugares()
while resp == "s" or resp == "S":
    reser = int(input("Reservar a cadeira: B"))
    if reser == lugar[reser - 1]:
        print("Cadeira {} Reservada!" .format(lugar[reser - 1]))
        lugar[reser - 1] = "---"
    else:
            print("Erro: Lugar ocupado!")
                   
           
    
    resp = input("Quer resevar outro? [S/N]")
    lugares()
    