import re

email1 = "Meu número é 12341234"
email2 = "Fale comigo em 91234-1234. Esse é meu telefone"
email3 = "12341234 é o meu celular"
email4 = "heuheueheuheu 9534-1254 haushaushaushaus 99631-2914 brbrbrbr 432112345"

padrao = "[0-9]{4,5}[-]?[0-9]{4}"

retorno = re.findall(padrao, email4)
print(retorno)
