#Desenvolvido por LaLunaInSky
#Github.com/lalunaInSky


#Importações
from customtkinter import CTk, CTkLabel,CTkButton
from funcionamento.dados import *
import os


#Função
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def clique_teclado(event):
    for c in range(0, 10):
        if event.keysym == f'{c}':
            mostrador_número_único(f'{c}', operação_atual_texto, histórico_texto, label_operação_atual, botões_à_bloquear)

    if event.keysym == 'comma':
            mostrador_número_único(',', operação_atual_texto, histórico_texto, label_operação_atual, botões_à_bloquear)

    if event.keysym == 'slash':
        mostrador_histórico('÷', histórico_texto, operação_atual_texto, label_operação_atual, botões_à_bloquear)

    if event.keysym == 'asterisk':
        mostrador_histórico('x', histórico_texto, operação_atual_texto, label_operação_atual, botões_à_bloquear)

    if event.keysym == 'Return':
        mostrador_histórico('=', histórico_texto, operação_atual_texto, label_operação_atual, botões_à_bloquear)

    if event.keysym == 'minus':
        mostrador_histórico('-', histórico_texto, operação_atual_texto, label_operação_atual, botões_à_bloquear)

    if event.keysym == 'plus':
        mostrador_histórico('+', histórico_texto, operação_atual_texto, label_operação_atual, botões_à_bloquear)

    if event.keysym == 'Delete':
        zerar_número_atual(operação_atual_texto, histórico_texto, label_operação_atual, botões_à_bloquear)

    if event.keysym == 'End':
        zerar_todo_o_programa(operação_atual_texto, histórico_texto, label_operação_atual, botões_à_bloquear)


#GUI
root = CTk()
root.title('Calculadora')
root.geometry('+600+200')
root.resizable(0, 0)
root.iconbitmap(resource_path('calculadora.ico'))


#Variáveis
histórico_texto = StringVar()
operação_atual_texto = StringVar()
operação_atual_texto.set('0')
botões_à_bloquear = []


#WIDGETS
label_histórico = CTkLabel(root, textvariable= histórico_texto, font= ('Arial', 13))
label_operação_atual = CTkLabel(root, textvariable= operação_atual_texto, font= ('Arial', 35, 'bold'))

button_porcentagem = CTkButton(
    root, text= '%', width= 90, height= 50, font= ('Arial', 15, 'bold'), fg_color= ('#404040'), hover_color= ('#666666'), text_color_disabled= ('#404040'),
    command= lambda: porcentagem(operação_atual_texto, histórico_texto)
)
botões_à_bloquear.append(button_porcentagem)


button_apagar_operação_atual = CTkButton(
    root, text= 'CE', width= 90, height= 50, font= ('Arial', 15, 'bold'), fg_color= ('#404040'), hover_color= ('#666666'),
    command= lambda: zerar_número_atual(operação_atual_texto, histórico_texto, label_operação_atual, botões_à_bloquear)
)

button_apagar_histórico_e_operações = CTkButton(
    root, text= 'C', width= 90, height= 50, font= ('Arial', 15, 'bold'), fg_color= ('#404040'), hover_color= ('#666666'),
    command= lambda: zerar_todo_o_programa(operação_atual_texto, histórico_texto, label_operação_atual, botões_à_bloquear)
)

button_operador_divisão = CTkButton(
    root, text= '÷', width= 90, height= 50, font= ('Arial', 18, 'bold'), fg_color= ('#404040'), hover_color= ('#666666'), text_color_disabled= ('#404040'),
    command= lambda: mostrador_histórico('÷', histórico_texto, operação_atual_texto, label_operação_atual, botões_à_bloquear)
)
botões_à_bloquear.append(button_operador_divisão)


button_número_7 = CTkButton(
    root, text= '7', width= 90, height= 50, font= ('Arial', 18, 'bold'), fg_color= ('#666666'), hover_color= ('#404040'),
    command= lambda: mostrador_número_único('7', operação_atual_texto, histórico_texto, label_operação_atual, botões_à_bloquear)
)


button_número_8 = CTkButton(
    root, text= '8', width= 90, height= 50, font= ('Arial', 18, 'bold'), fg_color= ('#666666'), hover_color= ('#404040'),
    command= lambda: mostrador_número_único('8', operação_atual_texto, histórico_texto, label_operação_atual, botões_à_bloquear)
)

button_número_9 = CTkButton(
    root, text= '9', width= 90, height= 50, font= ('Arial', 18, 'bold'), fg_color= ('#666666'), hover_color= ('#404040'),
    command= lambda: mostrador_número_único('9', operação_atual_texto, histórico_texto, label_operação_atual, botões_à_bloquear)
)

button_operador_multiplicação = CTkButton(
    root, text= 'X', width= 90, height= 50, font= ('Arial', 15, 'bold'), fg_color= ('#404040'), hover_color= ('#666666'), text_color_disabled= ('#404040'),
    command= lambda: mostrador_histórico('x', histórico_texto, operação_atual_texto, label_operação_atual, botões_à_bloquear)
)
botões_à_bloquear.append(button_operador_multiplicação)


button_número_4 = CTkButton(
    root, text= '4', width= 90, height= 50, font= ('Arial', 18, 'bold'), fg_color= ('#666666'), hover_color= ('#404040'),
    command= lambda: mostrador_número_único('4', operação_atual_texto, histórico_texto, label_operação_atual, botões_à_bloquear)
)

button_número_5 = CTkButton(
    root, text= '5', width= 90, height= 50, font= ('Arial', 18, 'bold'), fg_color= ('#666666'), hover_color= ('#404040'),
    command= lambda: mostrador_número_único('5', operação_atual_texto, histórico_texto, label_operação_atual, botões_à_bloquear)
)

button_número_6 = CTkButton(
    root, text= '6', width= 90, height= 50, font= ('Arial', 18, 'bold'), fg_color= ('#666666'), hover_color= ('#404040'),
    command= lambda: mostrador_número_único('6', operação_atual_texto, histórico_texto, label_operação_atual, botões_à_bloquear)
)

button_operador_subtração = CTkButton(
    root, text= '-', width= 90, height= 50, font= ('Arial', 15, 'bold'), fg_color= ('#404040'), hover_color= ('#666666'), text_color_disabled= ('#404040'),
    command= lambda: mostrador_histórico('-', histórico_texto, operação_atual_texto, label_operação_atual, botões_à_bloquear)
)
botões_à_bloquear.append(button_operador_subtração)


button_número_1 = CTkButton(
    root, text= '1', width= 90, height= 50, font= ('Arial', 18, 'bold'), fg_color= ('#666666'), hover_color= ('#404040'),
    command= lambda: mostrador_número_único('1', operação_atual_texto, histórico_texto, label_operação_atual, botões_à_bloquear)
)

button_número_2 = CTkButton(
    root, text= '2', width= 90, height= 50, font= ('Arial', 18, 'bold'), fg_color= ('#666666'), hover_color= ('#404040'),
    command= lambda: mostrador_número_único('2', operação_atual_texto, histórico_texto, label_operação_atual, botões_à_bloquear)
)

button_número_3 = CTkButton(
    root, text= '3', width= 90, height= 50, font= ('Arial', 18, 'bold'), fg_color= ('#666666'), hover_color= ('#404040'),
    command= lambda: mostrador_número_único('3', operação_atual_texto, histórico_texto, label_operação_atual, botões_à_bloquear)
)

button_operador_adição = CTkButton(
    root, text= '+', width= 90, height= 50, font= ('Arial', 15, 'bold'), fg_color= ('#404040'), hover_color= ('#666666'), text_color_disabled= ('#404040'),
    command= lambda: mostrador_histórico('+', histórico_texto, operação_atual_texto, label_operação_atual, botões_à_bloquear)
)
botões_à_bloquear.append(button_operador_adição)


button_mudar_número_negativo_positivo = CTkButton(
    root, text= '+/-', width= 90, height= 50, font= ('Arial', 15, 'bold'), fg_color= ('#666666'), hover_color= ('#404040'), text_color_disabled= ('#404040'),
    command= lambda: positivo_ou_negativo(operação_atual_texto)
)
botões_à_bloquear.append(button_mudar_número_negativo_positivo)


button_número_0 = CTkButton(
    root, text= '0', width= 90, height= 50, font= ('Arial', 18, 'bold'), fg_color= ('#666666'), hover_color= ('#404040'),
    command= lambda: mostrador_número_único('0', operação_atual_texto, histórico_texto, label_operação_atual, botões_à_bloquear)
)

button_operador_vírgula = CTkButton(
    root, text= ',', width= 90, height= 50, font= ('Arial', 15, 'bold'), fg_color= ('#666666'), hover_color= ('#404040'), text_color_disabled= ('#404040'), 
    command= lambda: mostrador_número_único(',', operação_atual_texto, histórico_texto, label_operação_atual, botões_à_bloquear)
)
botões_à_bloquear.append(button_operador_vírgula)


button_operador_igualdade = CTkButton(
    root, text= '=', width= 90, height= 50, font= ('Arial', 15, 'bold'), fg_color= ('#009999'), hover_color= ('#004d4d'),
    command= lambda: mostrador_histórico('=', histórico_texto, operação_atual_texto, label_operação_atual, botões_à_bloquear)
)

label_desenvolvedora = CTkLabel(
    root, text= 'Desenvolvido por LaLunaInSky', font= ('Corbel', 14, 'bold')
)


#Binds
root.bind('<Key>', clique_teclado)


#LAYOUTS
label_histórico.grid(row= 0, columnspan= 4, sticky= E, padx= (0, 8), pady= (15, 0))
label_operação_atual.grid(row= 1, columnspan= 4, sticky= E, padx= (0, 8), pady= (20, 30))

button_porcentagem.grid(row= 2, column= 0, padx=(2, 2), pady= (0, 3))
button_apagar_operação_atual.grid(row= 2, column= 1, padx= (0, 2), pady= (0, 3))
button_apagar_histórico_e_operações.grid(row= 2, column= 2, padx= (0, 2), pady= (0, 3))
button_operador_divisão.grid(row= 2, column= 3, padx= (0, 2), pady= (0, 3))

button_número_7.grid(row= 3, column= 0, padx=(2, 2), pady= (0, 3))
button_número_8.grid(row= 3, column= 1, padx= (0, 2), pady= (0, 3))
button_número_9.grid(row= 3, column= 2, padx= (0, 2), pady= (0, 3))
button_operador_multiplicação.grid(row= 3, column= 3, padx= (0, 2), pady= (0, 3))

button_número_4.grid(row= 4, column= 0, padx=(2, 2), pady= (0, 3))
button_número_5.grid(row= 4, column= 1, padx= (0, 2), pady= (0, 3))
button_número_6.grid(row= 4, column= 2, padx= (0, 2), pady= (0, 3))
button_operador_subtração.grid(row= 4, column= 3, padx= (0, 2), pady= (0, 3))

button_número_1.grid(row= 5, column= 0, padx=(2, 2), pady= (0, 3))
button_número_2.grid(row= 5, column= 1, padx= (0, 2), pady= (0, 3))
button_número_3.grid(row= 5, column= 2, padx= (0, 2), pady= (0, 3))
button_operador_adição.grid(row= 5, column= 3, padx= (0, 2), pady= (0, 3))

button_mudar_número_negativo_positivo.grid(row= 6, column= 0, padx=(2, 2), pady= (0, 3))
button_número_0.grid(row= 6, column= 1, padx= (0, 2), pady= (0, 3))
button_operador_vírgula.grid(row= 6, column= 2, padx= (0, 2), pady= (0, 3))
button_operador_igualdade.grid(row= 6, column= 3, padx= (0, 2), pady= (0, 3))

label_desenvolvedora.grid(row=7, columnspan= 4, pady= (3, 3))

#GUI
root.mainloop()