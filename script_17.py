#listas em python
#-*- coding: utf-8 -*-
minha_lista = ["abacaxi","melancia", "abacate"]
minha_lista2 = [1,2,3,4,5]
minha_lista3 = ["abacaxi", 2, 9.89, True]

print(minha_lista)
print(minha_lista2)
print(minha_lista3)

print(minha_lista[0])#exibe determinado item da lista

for item in minha_lista:#imprime item por item
	print(item)

tamanho = len(minha_lista)

print(tamanho)#exibe a quantidade de elementos da lista

minha_lista.append("Limão")#adiciona limãp a minha_lista

print(minha_lista)

if 3 in minha_lista2:
      print("3 esta na lista") #procura se 3 esta em minha_lista2

del minha_lista[2:]#apagou os elementos da minha_lista : abacate e limão
print(minha_lista)

minha_lista4 = []

minha_lista4.append(57)
print(minha_lista4)

