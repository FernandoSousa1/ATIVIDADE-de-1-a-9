from tkinter import *
from tkinter import messagebox

def imp ():
    nome = str(entry_nome.get())
    peso = float(entry_peso.get())
    altura = float(entry_h.get())
    imc = peso * (altura**2)

    if peso < 40:
        messagebox.showwarning("Resultados", f"Bem-Vindo {nome}.\nSeu Peso: {peso} kg.\nSua Altura: {altura} m.\nSeu IMC: {imc}.\nSituação: Baixo Peso.")
    elif peso >= 50 and peso <= 60:
        messagebox.showwarning("Resultados", f"Bem-Vindo {nome}.\nSeu Peso: {peso} kg.\nSua Altura: {altura} m.\nSeu IMC: {imc}.\nSituação: Peso Normal.")
    elif peso >= 60 and peso <= 75:
        messagebox.showwarning("Resultados", f"Bem-Vindo {nome}.\nSeu Peso: {peso} kg.\nSua Altura: {altura} m.\nSeu IMC: {imc}.\nSituação: Excesso de Peso.")
    elif peso > 75 and peso <= 81:
        messagebox.showwarning("Resultados", f"Bem-Vindo {nome}.\nSeu Peso: {peso} kg.\nSua Altura: {altura} m.\nSeu IMC: {imc}.\nSituação: Obesidade.")
    elif peso > 81:
        messagebox.showwarning("Resultados", f"Bem-Vindo {nome}.\nSeu Peso: {peso} kg.\nSua Altura: {altura} m.\nSeu IMC: {imc}.\nSituação: Obesidade extrema.")

janela = Tk()

janela.geometry("800x400")
janela.title("Calculando IMC")

lbl_nome = Label(janela, text="Seu Nome:")
lbl_nome.place(x=10, y=10)

entry_nome = Entry(janela)
entry_nome.place(x=10, y=50)

lbl_peso = Label(janela, text="Seu Peso:")
lbl_peso.place(x=10, y=100)

entry_peso = Entry(janela)
entry_peso.place(x=10, y=150)

lbl_h = Label(janela, text="Sua Altura:")
lbl_h.place(x=10, y=200)

entry_h = Entry(janela)
entry_h.place(x=10, y=250)

btn_imp = Button(janela, text="Imprimir", command=imp)
btn_imp.place(x=10 , y=300)

janela.mainloop()