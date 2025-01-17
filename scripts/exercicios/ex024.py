cidade = input("Insira o nome da sua cidade: ")
cidade = cidade.split()


if cidade[0].upper().find('SANTO') == 0:
    print("O nome da sua cidade começa com Santo")
else: 
    print("O nome da sua cidade não começa com Santo")