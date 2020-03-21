
#manipulaçao de arquivos
# função open
# variavel = open(nome, modo)
"""
Modo Função 
r -  somente leitura
w -  escrita (Caso o arquivo ja exista, ele será apagado e um novo arquivo sera criado)
a -  leitura e escrita (adiciona o novo conteudo ao fim do arquivo)
r+ - leitura e escrita
w+ - escrita (o modo w+, assim como o w, também apaga o conteudo anterior do arquivo)
a+ - leitura e escrita (abre o arquivo para atualização)"""
#-*- coding: utf-8 -*-
arquivo = open("meuarquivo.txt")

linhas = arquivo.readlines() #vai ler o arquivo e jogar dentro de uma lista
print (linhas)

for linha in linhas:
	print (linha)

texto_completo = arquivo.read()
print(texto_completo)