#coding: utf8
import requests
import xmltodict
print("Digite o nome do usuário que deseja consultar")
nome = raw_input()
nome.lower
req = requests.get('https://api.github.com/users/'+nome)
saida = req.text
saida1 = saida.split(",")
lista = []
for i in saida1:
    lista.append(i.replace(":","#",1))

for i in lista:
    print(xmltodict.unparse({i.split("#")[0]:i.split("#")[1]}))
