#função enumerate

lista = ["Abacate", "Bola", "Cachorro"]
for i in lista:
	print(i)

for i in range(len(lista)):#imprime a posição do item e o nome do item
	print(i, lista[i])
	
#essa é a melhor maneira
for i, nome in enumerate(lista):#imprime a posição do item e o nome do item
	print(i, nome)
