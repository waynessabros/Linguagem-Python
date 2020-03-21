#zip

lista1=[1,2,3,4,5]
lista2=["Abacate", "Bola", "Cachorro", "Dinheiro", "Elefante"]
lista3=["R$ 2,OO","R$ 5,OO","Não tem preço","Não tem preço","Não tem preço"]
#concatena duas ou mais listas pra imprimir
for numero, nome, dinheiro in zip (lista1, lista2, lista3):
	print(numero, nome, dinheiro)