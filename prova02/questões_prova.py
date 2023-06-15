#1
import random

list01 = [random.randint(0, 20) for _ in range(50)]
soma = sum(list01)
print("Soma de valores: {}".format(soma))

num_9 = list01.count(9)
print("Número de vezes que o número 9 apareceu:{}".format(num_9))

maior_valor = max(list01)
print("Maior valor:", maior_valor)

maior_valor = [i for i, valor in enumerate(list01) 
    if valor == maior_valor]
print("Posições onde aparecem o maior valor: {}".format (maior_valor))

#2
sim = 0
resposta = input("Telefonou para a vítima ? (Sim ou Não): ")
if resposta.upper() == "Sim" or resposta.upper() =="S":
    sim += 1
resposta = input("Esteve no local do crime ? (Sim ou Não): ")
if resposta.upper() == "Sim" or resposta.upper() =="S":
    sim += 1
resposta = input("Mora perto da vítima ? (Sim ou Não): ")
if resposta.upper() == "Sim" or resposta.upper() =="S":
    sim += 1
resposta = input("Devia para a vítima ? (Sim ou Não): ")
if resposta.upper() == "Sim" or resposta.upper() =="S":
    sim += 1
resposta = input("Já trabalhou com a vítima ? (Sim ou Não): ")
if resposta.upper() == "Sim" or resposta.upper() =="S":
    sim += 1

if sim < 2:
    print("Inocente")
elif sim == 2:
    print("Suspeita")
elif sim < 5:
    print("Cúmplice")
else:
    print("Assassino")



#3
list = []
maior_que = 0
soma_1 = 0
soma_2 = 0
quantidade = 0

while True:
    num01 = float(input("Digite um valor inteiro (quando desejar parar digite um valor negativo): "))
    if num01 < 0:
        break

    list.append(num01)
    print(list)
    if num01 > 0:
        quantidade += 1
        print("Quantidade de valores armazenados:" .format(quantidade))
    if num01 > 5:
        maior_que += 1
        print ("Quantidade de números maiores que 5:".format (maior_que))
    if num01 % 2 == 0:
        soma_1 += 1
        print("A soma dos valores pares armazenados: {}" .format(soma_1))
    if num01 % 2 == 1:
        soma_2 += 1
        print("A soma dos valores ímpares armazenados: {}" .format(soma_2))
