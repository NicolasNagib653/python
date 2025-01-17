import tkinter

    

janela = tkinter.Tk()
janela.geometry("500x300")

texto = tkinter.Label(janela, text="Fazer Login")
texto.pack(padx= 10, pady=10)

botao = tkinter.Button(janela, text="Login")
botao.pack(padx= 10, pady=10)


janela.mainloop()