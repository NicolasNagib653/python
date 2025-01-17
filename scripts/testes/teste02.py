import requests
from tkinter import *
from tkinter import ttk

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()
    cotacao_bitcoin = requisicao_dic['BTCBRL']['bid']
    cotacao_dolar   = requisicao_dic['USDBRL']['bid']
    cotacao_euro    = requisicao_dic['EURBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro:  {cotacao_euro}
    Bitcoin: {cotacao_bitcoin}'''

    texto_cotacoes["text"] = texto




janela = Tk()
janela.title("Cotação atual das moedas")
texto_orientação = Label(janela, text="Clique no botão para ver as cotações das moedas")
texto_orientação.grid(column=0, row=0, padx= 20, pady=20)

botao = Button(janela, text="Buscar cotações", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=20,pady=10)

texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=0, row=2, padx=20,pady=20)
janela.mainloop()