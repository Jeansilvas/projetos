var_a = 9
var_a
type(var_a)
var_b = 7.75
type(var_b)
var_a != var_b
var_a * var_b
var_a ** var_b
var_a + var_b
var_a - var_b

idade, peso, altura = 32, 80, 1.75
idade, peso, altura
type(altura)
idade / peso

                  #Trabalhando com variaveis
a = 10
b = 3

a + b
a - b
a / b

v = a / b

type(v)
type(a)
v

                   #Resto da divisão

a % b

                   #Transformar números em str

p = 'Python é '
p + str(a)

                   #Converter tipos de variaveis


type(3)
type(5.6)
type('Jota ')
type(True)
type(None)  #<<<Sem definição!

isinstance(5.6, int)
isinstance(5.6, (int, float ))

float(5)
int(5.6)
str(7)
bool(0)
bool(1)
bool(5)   #<<<<< Bool acima ou abaixo de 0 sempre é verdadeiro
bool('')  #False
bool('S') #True


                                      #Indexação
         # A indexação no python é a sequência de dados contidos dentro da variavel e começa a partir de 0, é usado "[]""


var = 'Python'  #começa a partir de 0 na primeira str ou int
type(var)
len(var)  #Len retorna o tamanho da variavel no caso o número de caracteres
var[0]    #Retorna o indice de indexação correspondente a variavel
var[2]

var.find('P') #busca a posisão de indice da letra ou numero na variavel

#Slincing - Fatiamentos

frase = 'Eu vou me tornar um milionario!'
len(frase)

frase[0:2]
frase[12]
frase[0:31]
frase[-1] #-1 Retorna o ultimo dado da variavel seja srt, int, float, etc..
frase[::2] #:: Retorna a variavel na sequencia desejada como pular de 2 em 2 letras de uma frase
frase[::-1] #<< Retorna o valor invertido


             #LISTAS  >>>São definidas com colchetes[] ou built-in

L1 = [] #cria uma lista vazia []
type(L1)

L2 = list() #cria uma lista vazia built-in
type(L2)

N1 = ['Eu', 'Vou', 'Vencer'] #<<< 3 strngs
N2 = ['Eu vou VENCER'] #<<< 1 strgn

len(N1)         
len(N2)
N1[0]
N2[0]
N1[::2]

J1 = ['MILIONÁRIO', 33, 20.24]
type(J1)
len(J1)
type(J1[0])  #>>>> Retorna o tipo de variavel dentro de uma lista
type(J1[1])  #>>>> Retorna o tipo de variavel dentro de uma lista
type(J1[2])  #>>>> Retorna o tipo de variavel dentro de uma lista

del N1[0]    #>>> Deleta uma variavel dentro de uma lista
N1
N1.remove('Vou') #Também deleta uma variavel dentro de uma lista
N1


                                 #Aninhar listas


lista = [[10, 20, 30], [15, 25, 35], [100, 200, 300, 400, 500]]
type(lista)
len(lista)

lista[0]
lista[0][1] #Retorna o valor da variavel dentro da lista interna
lista[2][3] #Primeiro colchetes indice, segundo colchetes elemento


                                 #Métodos


LISTA = [1, 2, 4, 8, 12, 33]
LISTA1 = [3, 5, 7, 11, 13, 30]
L = LISTA + LISTA1
L
L.sort()     #Retorna os valores em ordem crescente
L
L.reverse() #Retorna os valores em ordem reversa
L
                 
                                     #CÓPIA DE LISTA


v = LISTA[:]  #Para mudanças na lista sem alterar a matriz se faz a cópia
v1 = LISTA.copy()  #Para mudanças na lista sem alterar a matriz se faz a cópia
v.append(9)
v
v1
v1.append(67)
v1
v
LISTA    #Lista copiada sem alterações


                                  ###DICIONARIOS###


h = ['Luiz', 2000, 'Sid', 1980, 'Fabio', 2200]
p = {'Luiz':1980, 'Sid':2000, 'Fabio':2200}
type(h)
type(p)
h
p
p['Sid']
p.keys()
p.values()
k = {'Sergio':2500}
p.update(k) #insere valores ao dicionario
p
p.items()

                                #VETORES ARRAYS


import numpy as np


v = np.array([1, 2, 3, 4, 5, 6])


                                #ESTRUTURA IF

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))

if(a > b):
    print(a, 'a é maior que', b)
if(b > a):
    print(b, 'b é maior que ', a)
                                

                                #ESTRUTURA ELSE

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))

if(a > b):
    print(a, 'a é maior que', b)
else:
    print(b, 'b é maior que ', a)

                                   #CONDICIONAIS

idade = int(input('Digite sua idade: '))
sexo = int(input('1 Feminino 2 Masculino: '))

if idade >= 9 and idade <= 12:
    print('É uma criança')
    if sexo == 2:
        print('Sexo Masculino')
    else: print('Sexo Feminino')


if idade >= 13 and idade <= 17:
    print('É um(a) adolescente')
    if sexo == 2:
        print('Sexo Masculino')
    else: print('Sexo Feminino')


                                    #CONDICIONAL ELIF

idade = int(input('Digite sua idade: '))
sexo = int(input('M1 F2: '))

if idade >= 9 and idade <=12:
    print('É uma criança')
elif idade >= 13 and idade <= 17:
    print('É um(a) adolescente')
elif idade >= 18 and idade <= 22:
    print('É maior de idade')
elif idade >= 23 and idade <= 27:
    print('É melhor estar estruturado')
elif idade >= 28 and idade <= 35:
    print('MILIONARIO')

if sexo == 1:
    print('Sexo Masculino')
else:
    print('Sexo Feminino')


                                        #LOOP FOR

for i in range(0, 10, 2):  #Numero inicial, numero final, numero de contagem.
    print(i)

                                         #Laço for em Estrutura de dados

lista = [3, 8, 44, 2, 1, 7, 12, 6, 5]

for i in lista:  #Retorna todos os elementos da lista
    print(i)

lista = [3, 8, 44, 2, 1, 7, 12, 6, 5]

for i in lista:      #Retorna os valores pares dentro da lista
    if i % 2 == 0:
        print(i)

lista = [3, 8, 44, 2, 1, 7, 12, 6, 5]

for i in lista:
    if i % 2 != 0:   #Retorna os valores impares dantro da lista
        print(i)


                                             #LAÇO WHILE

k = 0

while k <= 10:
    print(k)
    k = k + 1    #<<<CONTADOR COM WHILE

                                        # pass, break e continue

for letra in 'programador':
    if letra == 'a':
        pass  #<<<<PASSA PARA A FUNÇÂO SEGUINTE
    print(letra)

for letra in 'programador':
    if letra == 'a':
        continue  #<<<<<<RETORNA SEM A LETRA A
    print(letra)

for letra in 'programador':
    if letra == 'a':
        break  #<<<INTERROMPE NO VALOR INDICADO A
    print(letra)

                                     #Funções

def print_text():   #<<<Função (print_text) criada!
    print('Sou um Vencedor!')

print_text()

def print_isto(x):  #Função criada com exigencia de argumento: (x)
    print(x)

lista = [1, 2, 4, 6, 7, 'RICO']
print_isto(1234)
print_isto('MILIONÀRIO')
print_isto(lista)


def potencia(x):  #EXEMPLO DE FUNÇÂO DE POTENCIA
    p = x ** 2  #EXEMPLO DE FUNÇÂO DE POTENCIA
    return p  #EXEMPLO DE FUNÇÂO DE POTENCIA

print(potencia(4))  #EXEMPLO DE FUNÇÂO DE POTENCIA

def potencia_n(x, n = 2):
    p = x ** n
    return p

print(potencia_n(5))

def soma(a, b):
    return(a + b)

print(soma(20, 44))

def conta(*valores):
    soma = 0
    for i in valores:
        soma = soma + i
    return print(soma)

conta(44, 67, 88, 99, 200, 55)

#############################################JANELA##################
from tkinter import *

janela = Tk()

janela.title('JOTA')




janela.mainloop()
######################################################################

print('-------ADIVINHE O NUMERO---------')

numero = int(input('Digite o seu palpite: '))

if numero != 20:
    print('Infelizmente ', numero, ' não é o numero certo')
    pass
if numero == 20:
    print('Parabéns o numero secreto era', numero)
