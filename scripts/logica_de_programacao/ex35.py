Mai = 0
def topo():
    print("----------------------------------------")
    print(" D E T E C T O R    D E     P E S A D O ")
    print(" Maior peso até agora: {} Kg " .format(Mai))
    print("----------------------------------------")

topo()


for i in range(0, 5):
    n = input("Digite o nome: ")
    p = int(input("Digite o peso de {}: " .format(n)))

    if p > Mai:
        Mai    = p
        Pesado = n
    topo()

topo()
print("A pessoa mais pesada foi {} com {} quilos" .format(Pesado, Mai))