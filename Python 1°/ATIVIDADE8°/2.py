from tkinter import *
from tkinter import messagebox

def imp():
    nome = str(entry_nome.get())
    genero = str(entry_g.get())
    altura = float(h.get())
    peso = float(p.get())
    imc = peso * (altura**2)

    if imc <= 18.5:
        messagebox.showwarning("Resultados", f"Bem-Vindo {nome}.\nSeu Genero é {genero}.\nSeu Peso: {peso} kg.\nSua Altura: {altura} m.\nSeu IMC: {imc}.\nSituação: Baixo Peso.")
    elif imc >= 18.5 and imc <= 24.9:
        messagebox.showwarning("Resultados", f"Bem-Vindo {nome}.\nSeu Genero é {genero}.\nSeu Peso: {peso} kg.\nSua Altura: {altura} m.\nSeu IMC: {imc}.\nSituação: Peso Normal.")
    elif imc >= 25 and imc <= 29.9:
        messagebox.showwarning("Resultados", f"Bem-Vindo {nome}.\nSeu Genero é {genero}.\nSeu Peso: {peso} kg.\nSua Altura: {altura} m.\nSeu IMC: {imc}.\nSituação: Excesso de Peso.")
    elif imc >= 30 and imc <= 35:
        messagebox.showwarning("Resultados", f"Bem-Vindo {nome}.\nSeu Genero é {genero}.\nSeu Peso: {peso} kg.\nSua Altura: {altura} m.\nSeu IMC: {imc}.\nSituação: Obesidade.")
    elif imc >= 35:
        messagebox.showwarning("Resultados", f"Bem-Vindo {nome}.\nSeu Genero é {genero}.\nSeu Peso: {peso} kg.\nSua Altura: {altura} m.\nSeu IMC: {imc}.\nSituação: Obesidade extrema.")

janela = Tk()

janela.geometry("800x400")
janela.title("Calculando IMC + Genero")

lbl_nome = Label(janela, text="Seu Nome:")
lbl_nome.place(x=10, y=10)

entry_nome = Entry(janela)
entry_nome.place(x=10, y=50)

lbl_peso = Label(janela, text="Seu Peso:")
lbl_peso.place(x=10, y=100)

p = entry_peso = Entry(janela)
entry_peso.place(x=10, y=150)

lbl_h = Label(janela, text="Sua Altura:")
lbl_h.place(x=10, y=200)

h = entry_h = Entry(janela)
entry_h.place(x=10, y=250)

lbl_g = Label(janela, text="Seu Genero:")
lbl_g.place(x=200, y=10)

entry_g = Entry(janela)
entry_g.place(x=200, y=50)

btn_imp = Button(janela, text="Imprimir", command=imp)
btn_imp.place(x=200, y=150)

janela.mainloop()