'''
argumento = "https://www.bytebank.com.br/cambio?moedaorigem=real"

subString = argumento[5:11]
print(subString)
'''

argumento = "https://www.bytebank.com.br/cambio?moedaorigem=real"
index = argumento.find('=')
subString = argumento[index + 1:]
print(subString)

# ---

argumento2 = "moedaorigem=real"
listaargumentos = argumento2.split("=")
print(listaargumentos)

# ---

url = "pagina?argumentos"
indice = url.find("?")
print(url[indice + 1:])
