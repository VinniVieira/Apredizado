from tkinter import *
from tkinter import ttk

# cores
cor1 = "#FFFFFF" #branco
cor2 = "#000000" #preto
cor3 = "#E58B26" #Laranja
cor4 = "#27ADE6" #Azul
cor5 = "#919191" #cinza

# Criar um janela no tk

janela = Tk()
janela.title ("calculadora")
janela.geometry("400x390")
janela.resizable(0,0)

frame_tela = Frame (janela, width=400, height=50, bg=cor5)
frame_tela.grid(row=0, column=0)

buton_frame = Frame (janela, width=400, height=450)
buton_frame.grid(row=1, column=0)

# Variável global para armazenar a expressão
expressao = ""

# Funções
def entrar_valores(event):
    global expressao
    texto = event
    if texto == "C":
        expressao = ""
    else:
        expressao += str(texto)
    input_text.set(expressao)

def calcular():
    global expressao
    try:
        resultado = str(eval(expressao))
        input_text.set(resultado)
        expressao = resultado
    except:
        input_text.set("Erro")
        expressao = ""

# criando label

input_text = StringVar()

tela_num = Label (frame_tela, textvariable=input_text, width=56, height=3,pady=7, anchor= "e", bg=cor5)
tela_num.place(x=0,y=0)


#buttoes

b_1clear = Button(buton_frame, text="C", width=13, height=5, command=lambda: entrar_valores("C"))
b_1clear.place(x=0, y=0)

b_porcento = Button(buton_frame, text="0", width=13, height=5, command=lambda: entrar_valores("0"))
b_porcento.place(x=100, y=0)

b_igual = Button(buton_frame, text="=", width=13, height=5, bg=cor4, fg=cor1, command=calcular)
b_igual.place(x=200, y=0)

b_divisao = Button(buton_frame, text="/", width=13, height=5, bg=cor4, fg=cor1, command=lambda: entrar_valores("/"))
b_divisao.place(x=300, y=0)

b_1 = Button(buton_frame, text="1", width=13, height=5, command=lambda: entrar_valores(1))
b_1.place(x=0, y=85)

b_2 = Button(buton_frame, text="2", width=13, height=5, command=lambda: entrar_valores(2))
b_2.place(x=100, y=85)

b_3 = Button(buton_frame, text="3", width=13, height=5, command=lambda: entrar_valores(3))
b_3.place(x=200, y=85)

b_multiplicacao = Button(buton_frame, text="x", width=13, height=5, bg=cor4, fg=cor1, command=lambda: entrar_valores("*"))
b_multiplicacao.place(x=300, y=85)

b_4 = Button(buton_frame, text="4", width=13, height=5, command=lambda: entrar_valores(4))
b_4.place(x=0, y=170)

b_5 = Button(buton_frame, text="5", width=13, height=5, command=lambda: entrar_valores(5))
b_5.place(x=100, y=170)

b_6 = Button(buton_frame, text="6", width=13, height=5, command=lambda: entrar_valores(6))
b_6.place(x=200, y=170)

b_soma = Button(buton_frame, text="+", width=13, height=5, bg=cor4, fg=cor1, command=lambda: entrar_valores("+"))
b_soma.place(x=300, y=170)

b_7 = Button(buton_frame, text="7", width=13, height=5, command=lambda: entrar_valores(7))
b_7.place(x=0, y=255)

b_8 = Button(buton_frame, text="8", width=13, height=5, command=lambda: entrar_valores(8))
b_8.place(x=100, y=255)

b_9 = Button(buton_frame, text="9", width=13, height=5, command=lambda: entrar_valores(9))
b_9.place(x=200, y=255)

b_subtracao = Button(buton_frame, text="-", width=13, height=5, bg=cor4, fg=cor1, command=lambda: entrar_valores("-"))
b_subtracao.place(x=300, y=255)

b_0 = Button(buton_frame, text="0", width=13, height=5, command=lambda: entrar_valores(0))
b_0.place(x=0, y=340)

b_ponto = Button(buton_frame, text=".", width=13, height=5, command=lambda: entrar_valores("."))
b_ponto.place(x=100, y=340)




janela.mainloop()