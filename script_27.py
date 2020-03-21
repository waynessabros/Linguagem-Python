#Map
def dobro(x):
	return x*2

valor = [1, 2, 3,4,5]
#quando vc multiplica uma lista por 2, você esta apenas exibindo ela duas vezes
print(dobro(valor))
#como dobrar o valor de uma lista
valor_dobrado = (map(dobro, valor))

for v in valor_dobrado:
	print(v)