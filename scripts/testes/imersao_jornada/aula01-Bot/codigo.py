import pyautogui
import time
import pandas
# 29106
# Passo 1: abrir o site

pyautogui.PAUSE= 1
pyautogui.press("win")
pyautogui.write("google")
pyautogui.press("enter")
time.sleep(2)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)
# passo 2: logar no sistema

pyautogui.click(x=936, y=327)
pyautogui.write("robsom@gmail.com")
pyautogui.press("tab")

pyautogui.write("senha")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

# Passo 3: importar a base de dados
tabela = pandas.read_csv("produtos.csv")
print(tabela)
# Passo 4: Cadastrar 1 produto

# # cod 
# pyautogui.click()
# pyautogui.write("MOLO000251")
# pyautogui.press("tab")

# # marca 
# pyautogui.write("Logitech")
# pyautogui.press("tab")

# # tipo
# pyautogui.write("Mouse")
# pyautogui.press("tab")

# # categoria
# pyautogui.write("1")
# pyautogui.press("tab")

# # preço unitário
# pyautogui.write("25.95")
# pyautogui.press("tab")

# # custo
# pyautogui.write("6.5")
# pyautogui.press("tab")

# # obs 
# pyautogui.write("")
# pyautogui.press("tab")
# pyautogui.press("enter")


# Passo 5: Repetir o passo 4 até acabar todos os produtos
for linha in tabela.index:
    # cod 
    pyautogui.click(x=916, y=250)
    cod = tabela.loc[linha, "codigo"]
    pyautogui.write(str(cod))
    pyautogui.press("tab")

    # marca 
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria = tabela.loc[linha,"categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preço unitário
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    # custo
    custo = tabela.loc[linha,"custo"]
    pyautogui.write("6.5")
    pyautogui.press("tab")

    # obs 
    obs = str(tabela.loc[linha,"obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000000)

# for linha in tabela.index
