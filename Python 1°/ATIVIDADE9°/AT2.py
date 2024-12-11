from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import simpledialog

def I():
    def imp():
        peso = float(Entry_p.get())
        altura = float(Entry_h.get())
        nome = str(Entry_n.get())
        imc = peso / (altura**2)
        messagebox.showinfo("Resutados", f"Bem-Vindo {nome}\nVocê pesa {peso}\nE sua altura é de {altura}\nSeu IMC:{imc}")
    janela2 = Toplevel()
    janela2.title("IMC")
    janela2.geometry("400x400")
    
    lbl_p = Label(janela2, text="Informe Sua Massa:")
    lbl_p.place(x=1, y=10)
    Entry_p = ttk.Entry(janela2)
    Entry_p.place(x=1, y=50)
    
    lbl_h = Label(janela2, text="Informe Sua Altura:")
    lbl_h.place(x=1, y=90)
    Entry_h = ttk.Entry(janela2)
    Entry_h.place(x=1, y=130)
    
    lbl_n = Label(janela2, text="Informe Seu Nome:")
    lbl_n.place(x=1, y=170)
    Entry_n = ttk.Entry(janela2)
    Entry_n.place(x=1, y=210)
    
    btn_imp = ttk.Button(janela2, text="Imprimir", command=imp)
    btn_imp.place(x=1, y=250)
def r3():
    def imp():
        a = float(Entry_a.get())
        b = float(Entry_b.get())
        c = float(Entry_c.get())
        x = float(a/(b*c))
        messagebox.showinfo("Resutados", f"O resutado obtido foi de X = {x}")
    janela3 = Toplevel()
    janela3.title("Regra de Três")
    janela3.geometry("400x400")
    
    lbl_a = ttk.Label(janela3, text="Informe valor A:")
    lbl_a.place(x=1, y=10)
    Entry_a = ttk.Entry(janela3)
    Entry_a.place(x=1, y=40)
    
    lbl_b = ttk.Label(janela3, text="Informe valor B:")
    lbl_b.place(x=150, y=10)
    Entry_b = ttk.Entry(janela3)
    Entry_b.place(x=150, y=40)
    
    lbl_c = ttk.Label(janela3, text="Informe valor C:")
    lbl_c.place(x=1, y=70)
    Entry_c = ttk.Entry(janela3)
    Entry_c.place(x=1, y=100)

    lbl_x = ttk.Label(janela3, text="valor X")
    lbl_x.place(x=150, y=100)

    btn_imp = ttk.Button(janela3, text="Calcular", command=imp)
    btn_imp.place(x=1, y=150, width="400")
def ka ():
    janela4 = Toplevel()
    janela4.title("Calculadora")
    janela4.geometry("400x400")

    

    btn_1 = ttk.Button(janela4, text="1")
    btn_1.place(x=1, y=1 )
    
    btn_2 = ttk.Button(janela4, text="2")
    btn_2.place(x=75, y=1 )
    
    btn_3 = ttk.Button(janela4, text="3")
    btn_3.place(x=148, y=1 )
    
    btn_d = ttk.Button(janela4, text="/")
    btn_d.place(x=222, y=1 )

    btn_4 = ttk.Button(janela4, text="4")
    btn_4.place(x=1, y=75 )
    
    btn_5 = ttk.Button(janela4, text="5")
    btn_5.place(x=75, y=75)

    btn_6 = ttk.Button(janela4, text="6")
    btn_6.place(x=148, y=75)

    btn_m = ttk.Button(janela4, text="*")
    btn_m.place(x=222, y=75 )

    btn_7 = ttk.Button(janela4, text="7")
    btn_7.place(x=1, y=148 )

    btn_8 = ttk.Button(janela4, text="8")
    btn_8.place(x=75, y=148 )

    btn_9 = ttk.Button(janela4, text="9")
    btn_9.place(x=148, y=148 )

    btn_s = ttk.Button(janela4, text="-")
    btn_s.place(x=222, y=148 )

    btn_0 = ttk.Button(janela4, text="0")
    btn_0.place(x=75, y=222 )

    btn_po = ttk.Button(janela4, text=".")
    btn_po.place(x=1, y=222 )

    btn_rc = ttk.Button(janela4, text="=")
    btn_rc.place(x=222, y=222 )

    btn_sm = ttk.Button(janela4, text="+")
    btn_sm.place(x=148, y=222 )

janela = Tk()

janela.title("Site do Carlinhos")
janela.geometry("300x200")

btn_IMC = ttk.Button(janela, text="IMC", command=I)
btn_IMC.place(x=1 , y=10, width=100)

btn_r3 = ttk.Button(janela, text="Regra de três", command=r3)
btn_r3.place(x=1 , y=50, width=100)

btn_ca = ttk.Button(janela, text="Calculadora", command=ka)
btn_ca.place(x=1 , y=90, width=100)

lbl_f = ttk.Label(janela, text="Bem-Vindo a o Site do Carlinhos\n\t🥳🥳🥳🥳🥳🥳")
lbl_f.place(x=120, y=50)

janela.mainloop()