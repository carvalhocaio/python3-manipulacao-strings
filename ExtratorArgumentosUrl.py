class ExtratorArgumentosUrl:
    def __init__(self, url):
        if self.stringEhValida(url):
            self.url = url.lower()
        else:
            raise LookupError("Url inválida!")

    def __len__(self):
        return len(self.url)

    def __str__(self):
        moedaOrigem, moedaDestino = self.retornaMoedas()
        # representacaoString = "Valor: " + self.extraiValor() + " " + moedaOrigem + " " + moedaDestino
        representacaoString2 = "Valor: {}\n Moeda Origem: {}\n Moeda Destino: {}\n".format(self.extraiValor(),
                                                                                           moedaOrigem, moedaDestino)
        return representacaoString2

    def __eq__(self, outraInstancia):
        return self.url == outraInstancia.url

    @staticmethod
    def stringEhValida(url):
        if url and url.startswith("https://bytebank.com"):
            return True
        else:
            return False

    def retornaMoedas(self):

        buscaMoedaOrigem = "moedaorigem=".lower()
        buscaMoedaDestino = "moedadestino=".lower()

        indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
        indiceFinalMoedaOrigem = self.url.find("&")

        moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]

        if moedaOrigem == "moedadestino":
            self.trocaMoedaOrigem()
            indiceInicialMoedaOrigem = self.encontraIndiceInicial(
                buscaMoedaOrigem)
            indiceFinalMoedaOrigem = self.url.find("&")
            moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]

        indiceInicialMoedaDestino = self.encontraIndiceInicial(
            buscaMoedaDestino)
        indiceFinalMoedaDestino = self.url.find("&valor")

        moedaDestino = self.url[indiceInicialMoedaDestino:indiceFinalMoedaDestino]

        return moedaOrigem, moedaDestino

    def encontraIndiceInicial(self, moedaOuValor):
        return self.url.find(moedaOuValor) + len(moedaOuValor)

    def trocaMoedaOrigem(self):
        self.url = self.url.replace("moedadestino", "real", 1)
        print(self.url)

    def extraiValor(self):
        buscaValor = "valor="
        indiceInicialValor = self.encontraIndiceInicial(buscaValor)
        valor = self.url[indiceInicialValor:]
        return valor
