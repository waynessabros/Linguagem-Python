#dicionarios são listas de associações compostas por: uma chave e um valor correspondente
# dicionario = {'chave':'valor'}
meu_dicionario = {"A":"AMEIXA","B":"BOLA", "C":"CACHORRO"}

print(meu_dicionario["A"])
print(meu_dicionario)

#navegação
for chave in meu_dicionario:
	print(chave+"-"+meu_dicionario[chave])

for chave in meu_dicionario.keys():
	print(chave)