#Desenvolvido por LaLunaInSky
#Github.com/lalunaInSky

from funcionamento.transformações import *

def adiciona_pontos_no_resultado(resultado):
    números = []

    if resultado.count(',') != 0:
        posição_vírgula = resultado.index(',')

        for posição, item in enumerate(resultado):
            if posição < posição_vírgula:
                números.append(item)
                adiciona_ponto_nos_números(números)
            else:
                números.append(item)
    else:
        print(resultado)
        for item in resultado:
            if item != '-':
                números.append(item)
                adiciona_ponto_nos_números(números)
        
        if resultado[0] == '-':
            números.insert(0, resultado[0])

    print(números)
    return tranforma_lista_em_string(números)


def adição(número_1, número_2):
    número_1 = transforma_vírgula_em_ponto(número_1)
    número_2 =  transforma_vírgula_em_ponto(número_2)
    
    resultado = número_1 + número_2
    resultado = arredondador_depois_do_ponto(str(resultado))
    return resultado


def subtração(número_1, número_2):
    número_1 = transforma_vírgula_em_ponto(número_1)
    número_2 =  transforma_vírgula_em_ponto(número_2)

    resultado = número_1 - número_2
    resultado = arredondador_depois_do_ponto(str(resultado))
    return resultado


def multiplicação(número_1, número_2):
    número_1 = transforma_vírgula_em_ponto(número_1)
    número_2 =  transforma_vírgula_em_ponto(número_2)
    
    resultado = número_1 * número_2
    resultado = arredondador_depois_do_ponto(str(resultado))
    return resultado


def divisão(número_1, número_2):
    número_1 = transforma_vírgula_em_ponto(número_1)
    número_2 =  transforma_vírgula_em_ponto(número_2)

    try:
        resultado = número_1 / número_2
        resultado = arredondador_depois_do_ponto(str(resultado))

        return resultado

    except ZeroDivisionError:
        return 'não é possível dividir por 0'


def porcentagem_calculo(número_1, número_2, operador):
    número_1 = transforma_vírgula_em_ponto(número_1)
    número_2 = transforma_vírgula_em_ponto(número_2)

    if operador == 'x' or operador == '÷':
        resultado = (número_1 / 100)
    else:
        resultado = (número_1 / 100) * número_2

    resultado = arredondador_depois_do_ponto(str(resultado))

    return resultado