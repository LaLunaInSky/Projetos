#Desenvolvido por LaLunaInSky
#Github.com/lalunaInSky

from customtkinter import *
from funcionamento.transformações import *
from funcionamento.operações import *

números_mostrador = []
repetido = [] 
histórico_números_e_operações = [] 
número_local = 0 
ultimo_número_local = 0 
sinal_negativo_ou_positivo = '' 

def positivo_ou_negativo(mostrador_número_único):
    global sinal_negativo_ou_positivo

    print(números_mostrador, sinal_negativo_ou_positivo)
    if números_mostrador != []:
        try:
            if sinal_negativo_ou_positivo == '':
                sinal_negativo_ou_positivo = '-'
                números_mostrador.insert(0, sinal_negativo_ou_positivo)
            else: 
                números_mostrador.remove(sinal_negativo_ou_positivo)
                sinal_negativo_ou_positivo = ''
            mostrador_número_único.set(tranforma_lista_em_string(números_mostrador))
        except:
            pass
    else:
        mostrador_número_único.set('0')


def porcentagem(mostrador_número_único, mostrador_histórico):
    if números_mostrador == [] or histórico_números_e_operações == []: 
        números_mostrador.clear() 
        números_mostrador.append('0') 
        mostrador_número_único.set(números_mostrador)
        números_mostrador.clear()
    
    if len(histórico_números_e_operações) == 2: 
        histórico_números_e_operações.append(
            porcentagem_calculo(
                analisador_depois_da_vírgula(números_mostrador), histórico_números_e_operações[0], histórico_números_e_operações[1]
            ).replace('.', ',')
        )

        mostrador_histórico.set(histórico_números_e_operações)
        números_mostrador.clear()
        números_mostrador.append(histórico_números_e_operações[2])
        mostrador_número_único.set(números_mostrador)


def zerar_todo_o_programa(mostrador_número_único, mostrador_histórico, label_número_único_mostrador, lista_de_botões_à_bloquear):
    global sinal_negativo_ou_positivo

    números_mostrador.clear()
    histórico_números_e_operações.clear()
    repetido.clear()
    sinal_negativo_ou_positivo = ''
    mostrador_histórico.set(histórico_números_e_operações)
    mostrador_número_único.set('0')

    analisador_tamanho_mostrador_número_único(
        label_número_único_mostrador, lista_de_botões_à_bloquear, números_mostrador, histórico_números_e_operações
    )


def zerar_número_atual(mostrador_número_único, mostrador_histórico, label_número_único_mostrador, lista_de_botões_à_bloquear):
    global sinal_negativo_ou_positivo
    
    números_mostrador.clear() 
    números_mostrador.append('0')
    sinal_negativo_ou_positivo = ''

    analisador_tamanho_mostrador_número_único(
        label_número_único_mostrador, lista_de_botões_à_bloquear, números_mostrador, histórico_números_e_operações
    )

    mostrador_número_único.set(tranforma_lista_em_string(números_mostrador))
    números_mostrador.clear()

    if histórico_números_e_operações == []: 
        mostrador_histórico.set(histórico_números_e_operações) 

        analisador_tamanho_mostrador_número_único(
            label_número_único_mostrador, lista_de_botões_à_bloquear, números_mostrador, histórico_números_e_operações
        )


def mostrador_número_único(número, mostrador_número_único, mostrador_histórico, label_número_único_mostrador, lista_de_botões_à_bloquear):
    mostrador_histórico.set(histórico_números_e_operações)
    
    global ultimo_número_local
    global número_local 
    número_local = número 

    try:
        if histórico_números_e_operações[0] == 'não é possível dividir por 0': 
            histórico_números_e_operações.clear() 
            mostrador_histórico.set(histórico_números_e_operações) 

    except: 
        pass 

    if ultimo_número_local == '' and número_local != '': 
        ultimo_número_local = número_local 
        números_mostrador.clear() 
        
        try: 
            if histórico_números_e_operações[3] == '=': 
                histórico_números_e_operações.clear() 
                mostrador_histórico.set(histórico_números_e_operações) 

        except: 
            pass 

    if len(números_mostrador) != 21: 
        números_mostrador.append(número_local) 
        
        if números_mostrador.count(',') == 0: 
            adiciona_ponto_nos_números(números_mostrador)

        else: 
            pass

        if números_mostrador.count(',') == 2: 
            números_mostrador.pop() 

        if números_mostrador[0] == ',': 
            números_mostrador.clear() 
            números_mostrador.append(mostrador_número_único.get())

        analisador_tamanho_mostrador_número_único(label_número_único_mostrador, lista_de_botões_à_bloquear, números_mostrador, histórico_números_e_operações)
   
    mostrador_número_único.set(tranforma_lista_em_string(números_mostrador)) 

    if números_mostrador[0] != número_local and len(números_mostrador) < 2:
        números_mostrador.clear()


def mostrador_histórico(operador, mostrador_histórico, mostrador_número_único, label_número_único_mostrador, lista_de_botões_à_bloquear):
    global ultimo_número_local
    global número_local
    ultimo_número_local = número_local

    if len(histórico_números_e_operações) == 0:
        if mostrador_número_único.get() == '0' and números_mostrador == []:
            números_mostrador.append(mostrador_número_único.get())

        histórico_números_e_operações.append(analisador_depois_da_vírgula(números_mostrador))
        mostrador_histórico.set(histórico_números_e_operações)
        números_mostrador.clear()     
    
    if len(histórico_números_e_operações) == 1:
        histórico_números_e_operações.append(operador)
        repetido.append(operador)
        mostrador_histórico.set(histórico_números_e_operações)

    if len(histórico_números_e_operações) == 2:
        analisador_tamanho_mostrador_número_único(
            label_número_único_mostrador, lista_de_botões_à_bloquear, números_mostrador, histórico_números_e_operações
        )
        
        if histórico_números_e_operações[1] == '=':
            if operador != '=':
                histórico_números_e_operações[1] = operador
                histórico_números_e_operações[0] = analisador_depois_da_vírgula(números_mostrador)

        try:
            if histórico_números_e_operações[1] == histórico_números_e_operações[2]:
                histórico_números_e_operações.pop()
                números_mostrador.clear()
        except:
            pass
        
        try:
            if histórico_números_e_operações[1] != operador and ultimo_número_local == '':
                histórico_números_e_operações.pop()
                histórico_números_e_operações.append(operador)
                repetido.clear()
                repetido.append(operador)
        except:
            pass
        
        if número_local != '' and ultimo_número_local != '' and tranforma_lista_em_string(números_mostrador) != '':
            repetido.clear()
            histórico_números_e_operações.append(analisador_depois_da_vírgula(números_mostrador))

        if mostrador_número_único.get() == "não é possível dividir por 0":
            números_mostrador.append('0')
            mostrador_número_único.set(números_mostrador)
            histórico_números_e_operações.clear()
            números_mostrador.clear()

        if histórico_números_e_operações[0] == '':
            histórico_números_e_operações[0] = '0'
            números_mostrador.append('0')
            mostrador_número_único.set(números_mostrador)
            números_mostrador.pop()

        try:
            if mostrador_número_único.get() != números_mostrador and histórico_números_e_operações[1] == repetido[1]:
                print(mostrador_número_único.get(), números_mostrador)
                números_mostrador.append(mostrador_número_único.get())
                histórico_números_e_operações.append(analisador_depois_da_vírgula(números_mostrador))
                mostrador_histórico.set(histórico_números_e_operações)
                print(mostrador_número_único.get(), números_mostrador)
                números_mostrador.clear()
        except:
            pass
            
        repetido.append(operador)
        mostrador_histórico.set(histórico_números_e_operações)

    if len(histórico_números_e_operações) == 3:
        repetido.clear()
        mostrador_histórico.set(histórico_números_e_operações)

        if histórico_números_e_operações[2] == '(':
            histórico_números_e_operações.pop()
            mostrador_histórico.set(histórico_números_e_operações)

        if operador == '=':
            if números_mostrador[0] == 'não é possível dividir por 0':
                histórico_números_e_operações.clear()
                números_mostrador.clear()
                números_mostrador.append('0')
                histórico_números_e_operações.append(números_mostrador)
                histórico_números_e_operações.append(operador)
                mostrador_número_único.set(números_mostrador)
                mostrador_histórico.set(histórico_números_e_operações)

                analisador_tamanho_mostrador_número_único(
                    label_número_único_mostrador, lista_de_botões_à_bloquear, números_mostrador, histórico_números_e_operações
                )

                números_mostrador.clear()
            else:
                histórico_números_e_operações.append(operador)
            
        else:
            try:
                if histórico_números_e_operações[1] == '+':
                    resultado = adição(histórico_números_e_operações[0], histórico_números_e_operações[2]).replace('.', ',')
                    
                if histórico_números_e_operações[1] == '-':
                    resultado = subtração(histórico_números_e_operações[0], histórico_números_e_operações[2]).replace('.', ',')

                if histórico_números_e_operações[1] == 'x':
                    resultado = multiplicação(histórico_números_e_operações[0], histórico_números_e_operações[2]).replace('.', ',')

                if histórico_números_e_operações[1] == '÷':
                    resultado = divisão(histórico_números_e_operações[0], histórico_números_e_operações[2]).replace('.', ',')

                números_mostrador.clear()
                histórico_números_e_operações.clear()
                histórico_números_e_operações.append(resultado)
                histórico_números_e_operações.append(operador)
                mostrador_número_único.set(adiciona_pontos_no_resultado(resultado))
                mostrador_histórico.set(histórico_números_e_operações)

                analisador_tamanho_mostrador_número_único(
                    label_número_único_mostrador, lista_de_botões_à_bloquear, números_mostrador, histórico_números_e_operações
                )  
            except:
                pass

    if len(histórico_números_e_operações) == 4:
        if operador != '=':
            histórico_números_e_operações[0] = analisador_depois_da_vírgula(números_mostrador)
            histórico_números_e_operações[1] = operador

            for c in range(1, 3):
                histórico_números_e_operações.pop()
            
            números_mostrador.clear()
            mostrador_histórico.set(histórico_números_e_operações) 
        
        try:
            if histórico_números_e_operações[3] == '=': 
                if histórico_números_e_operações[1] == '+': 
                    resultado = adição(histórico_números_e_operações[0], histórico_números_e_operações[2]).replace('.', ',')
                
                if histórico_números_e_operações[1] == '-': 
                    resultado = subtração(histórico_números_e_operações[0], histórico_números_e_operações[2]).replace('.', ',')

                if histórico_números_e_operações[1] == 'x': 
                    resultado = multiplicação(histórico_números_e_operações[0], histórico_números_e_operações[2]).replace('.', ',')

                if histórico_números_e_operações[1] == '÷': 
                    resultado = divisão(histórico_números_e_operações[0], histórico_números_e_operações[2]).replace('.', ',')

                números_mostrador.clear()
                números_mostrador.append(adiciona_pontos_no_resultado(resultado))

                analisador_tamanho_mostrador_número_único(
                    label_número_único_mostrador, lista_de_botões_à_bloquear, números_mostrador, histórico_números_e_operações
                ) 

            if resultado == 'não é possível dividir por 0': 
                histórico_números_e_operações.pop() 

            mostrador_histórico.set(histórico_números_e_operações)
            
            if operador == '=': 
                histórico_números_e_operações[0] = analisador_depois_da_vírgula(números_mostrador) 
                número_local = ''
                ultimo_número_local = número_local

            mostrador_número_único.set(números_mostrador) 
        except:
            pass

        analisador_tamanho_mostrador_número_único(
            label_número_único_mostrador, lista_de_botões_à_bloquear, números_mostrador, histórico_números_e_operações
        ) 

    número_local = ''