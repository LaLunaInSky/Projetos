#Desenvolvido por LaLunaInSky
#Github.com/lalunaInSky

from customtkinter import *

unidade = ''
dezena = ''
centena = ''

def arredondador_depois_do_ponto(número):
        posição_ponto = número.index('.')
        números_depois_do_ponto = vezes_repetidas = 0
        número_repetido = 0
        
        números_depois_do_ponto = número[posição_ponto + 1:]
        números_antes_do_ponto = número[:posição_ponto + 1]

        try:
                for contagem in range(0, 10):
                        if números_depois_do_ponto.count(f'{contagem}') > 3:
                                número_repetido = contagem
                                primeira_ocorrencia = números_depois_do_ponto.index(str(número_repetido))
                
                ultima_ocorrencia = primeira_ocorrencia + 3

                for contagem in range(primeira_ocorrencia, ultima_ocorrencia):
                        if int(números_depois_do_ponto[contagem]) == número_repetido:
                                vezes_repetidas += 1
        
                if vezes_repetidas == 1:
                        primeira_ocorrencia = números_depois_do_ponto.index(str(número_repetido), (primeira_ocorrencia + 1))
                        ultima_ocorrencia = primeira_ocorrencia + 3

                for contagem in range(primeira_ocorrencia, ultima_ocorrencia):
                        if int(números_depois_do_ponto[contagem]) == número_repetido:
                                vezes_repetidas += 1

        except:
                pass

        

        if vezes_repetidas > 2:
                return números_antes_do_ponto + números_depois_do_ponto[0:primeira_ocorrencia + 1]
        else:
              if len(números_depois_do_ponto) == 1 and números_depois_do_ponto == '0':
                return números_antes_do_ponto.replace('.', '')  
              else:
                return número


def transforma_vírgula_em_ponto(string):
    número = string.replace(',', '.')
    return float(número)


def tranforma_lista_em_string(lista):
        string_da_lista = ''

        for item in lista:
                string_da_lista += item
                
        return string_da_lista


def analisador_depois_da_vírgula(lista):
        string_da_lista = tranforma_lista_em_string(lista)
        string_separada = string_da_lista.partition(',')

        if len(string_separada[2]) != string_separada[2].count('0'):
                return string_da_lista.replace('.', '')
        else:
                return string_separada[0].replace('.', '')


def adiciona_ponto_nos_números(lista):
        global unidade
        global dezena
        global centena

        centena = dezena
        dezena = unidade
        
        if lista[len(lista) - 1].isnumeric():
                unidade = lista[len(lista) - 1]

        if centena != '' and len(lista) >= 4:
                if lista.count('.') >= 1:
                        if len(lista) == 6 or len(lista) == 10 or len(lista) == 14 or len(lista) == 18:
                                del lista[1]
                                lista.insert(2, '.')

                                if lista.count('.') >= 2:
                                        del lista[5]
                                        lista.insert(6, '.')

                                        if lista.count('.') >= 3:
                                                del lista[9]
                                                lista.insert(10, '.')

                                                if lista.count('.') >= 4:
                                                        del lista[13]
                                                        lista.insert(14, '.')

                        if len(lista) == 7 or len(lista) == 11 or len(lista) == 15 or len(lista) == 19:
                                del lista[2]
                                lista.insert(3, '.')

                                if lista.count('.') >= 2:
                                        del lista[6]
                                        lista.insert(7, '.')

                                        if lista.count('.') >= 3:
                                                del lista[10]
                                                lista.insert(11, '.')

                                                if lista.count('.') >= 4:
                                                        del lista[14]
                                                        lista.insert(15, '.')

                        if len(lista) == 8 or len(lista) == 12 or len(lista) == 16 or len(lista) == 20:
                                del lista[3]
                                lista.insert(4, '.')

                                if lista.count('.') >= 2:
                                        del lista[7]
                                        lista.insert(8, '.')

                                        if lista.count('.') >= 3:
                                                del lista[11]
                                                lista.insert(12, '.')

                                                if lista.count('.') >= 4:
                                                        del lista[15]
                                                        lista.insert(16, '.')
                try:
                        if lista.count('.') == 0 or lista[4] == '.' or lista[8] == '.' or lista[12] == '.': #adiciona os pontos novos
                                lista.insert(1, '.')
                except:
                        pass


def analisador_tamanho_mostrador_número_único(label, lista_de_botões, números_mostrador, histórico_números_e_operações):
        font = label.cget('font')
        try:
                if histórico_números_e_operações[1] == '=':
                        font = ('Arial', 35, 'bold')
                        label.grid(row= 1, columnspan= 4, sticky= E, padx= (0, 8), pady= (20, 30))
        except:
                pass
        
        try:
                if len(números_mostrador) > 19 or len(números_mostrador[0]) > 19:
                        font = ('Arial', 30, 'bold')
                        label.grid(row= 1, columnspan= 4, sticky= E, padx= (0, 8), pady= (23, 33))
                else:
                        font = ('Arial', 35, 'bold')
                        label.grid(row= 1, columnspan= 4, sticky= E, padx= (0, 8), pady= (20, 30))
        except:
               pass

        try:
                if números_mostrador[0] == 'não é possível dividir por 0':
                        font = ('Arial', 25, 'bold')
                        label.grid(row= 1, columnspan= 4, sticky= N, padx= (0, 8), pady= (26, 36))

                elif números_mostrador[0] != 'não é possível dividir por 0' and len(números_mostrador) < 1:
                        font = ('Arial', 35, 'bold')
                        label.grid(row= 1, columnspan= 4, sticky= E, padx= (0, 8), pady= (20, 30))
                        

        except:
                pass

        label.configure(font= font)

        for item in lista_de_botões:
                if font == ('Arial', 25, 'bold'):
                        item.configure(state= 'disabled')
                        item.configure(fg_color= ('#1a1a1a'))
                else:
                        item.configure(state= 'normal')
                
                        if item.cget('text') != '+/-' and item.cget('text') != ',':
                                item.configure(fg_color= ('#404040'))
                        else:
                                item.configure(fg_color= ('#666666'))