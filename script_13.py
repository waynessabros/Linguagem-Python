"""Em python strings são objetos
pode-se aplicar métodos a strings

string = string.metodo()
"""
#-*- coding: utf-8 -*-
a="Diego"
b="Mariana"
concatenar = a + " " + b

print(concatenar)
print(concatenar.lower())#lower = deixar tudo em minisculo
print(concatenar.upper())#upper = deixar tudo em maiusculo

concatenar2=concatenar.upper()
print(concatenar2)

#strip - Remove espaço e caracteres especiais
#split - converte a sequencia em lista
minha_string = "O rato roeu a roupa do rei de roma"
minha_lista = minha_string.split(" ")
print(minha_lista)

#como fazer busca na string
busca = minha_string.find("rei")#find procura onde esta a palavra em questão
print(busca)

print(minha_string[busca:])

busca2 = minha_string.find("rainha")
print(busca2)

minha_string2= minha_string.replace("o rei", "a rainha")
print(minha_string2)

