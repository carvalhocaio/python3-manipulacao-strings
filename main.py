from ExtratorArgumentosUrl import ExtratorArgumentosUrl

url = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500"

argumentoUrl = ExtratorArgumentosUrl(url)
argumentoUrl2 = ExtratorArgumentosUrl(url)

moedaOrigem, moedaDestino = argumentoUrl.retornaMoedas()
valor = argumentoUrl.extraiValor()
print(moedaDestino, moedaOrigem, valor)

# index = url.find("moedadestino") + len("moedadestino") + 1
# subString = url[index:]
# print(subString)

# string = 'bytebank'
# stringNova = string.replace('byte','Carvalho')
# print(stringNova)

# urlByteBank = 'https://bytebank.com'
# url1 = 'https://buscasites.com/busca?q=https://www.bytebank.com'
# url2 = 'https://bitebank.com.br'
# url3 = 'https://bytebank.com/cambio/teste/teste'
#
# print(url1.startswith(urlByteBank))
# print(url2.startswith(urlByteBank))
# print(url3.startswith(urlByteBank))

print(argumentoUrl)

print(argumentoUrl)
print(argumentoUrl2)

print(argumentoUrl == argumentoUrl2)
