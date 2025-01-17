from tkinter import *
def calculo_rg(): 
    rg = entrada.get()
    rgc = rg[0:len(rg)-1]
    print(f"RG completo {rg}")
    i = len(rg)
    n = 8
    final = 0
    for dig in reversed(rgc):
        sla = int(rgc[n-1]) * i
        final += sla
        texto_calculo["text"] += (f"{dig} * {i} = {sla}\n")
        i-=1
        n-=1
    texto_somatotal["text"] +=(f"A soma desses valores dá: {final}")
    resto = str(11-final%11)
    rgver = rgc+resto
    if(rg == rgver):
        if(resto == 10):
            texto_rgvalido["text"] = ("RG válido, digito verificador X")
        elif(resto == 11):
            texto_rgvalido["text"] = ("RG válido, digito verificador 0")
        else:
            texto_rgvalido["text"] = (f"RG válido, digito verificador: {resto}")
    if(rg != rgver):
        texto_rgvalido["text"] = ("RG inválido!!!")


janela = Tk()

janela.title("Calculo do RG")


texto_input = Label(janela, text="Insira seu RG: ")
texto_input.grid(column=0, row=0, pady=10)

entrada = Entry(janela, width=10)
entrada.grid(column=0, row=1, pady=10)


botao = Button(janela, text="Verificar RG", command=calculo_rg)
botao.grid(column=0, row=2, padx= 10, pady=10)

texto_calculo = Label(janela, text="")
texto_calculo.grid(column=0, row=3, padx= 10, pady=10)

texto_somatotal = Label(janela, text="")
texto_somatotal.grid(column=0, row=4, padx= 10, pady=10)

texto_rgvalido = Label(janela, text="")
texto_rgvalido.grid(column=0, row=5, padx= 10, pady=10)
janela.mainloop()