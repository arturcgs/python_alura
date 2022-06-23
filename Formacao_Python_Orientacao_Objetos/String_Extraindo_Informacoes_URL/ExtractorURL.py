import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    valores_moedas = {'dolar': 1, 'real': 5.24, 'peso_argentino': 124.08, 'euro': 0.95,
                      'libra': 0.82, 'iene': 134.84, 'dolar_canadense': 1.3}

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def valida_url(self):
        #verificando se a url está vazia
        if not self.url:
            raise ValueError('URL vazia')
        #procurando padrao de URL
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError('URL inválida')

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        return self.url[:indice_interrogacao]

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        return self.url[indice_interrogacao + 1:]

    def get_valor_parametro(self, parametro_busca):
        url_parametros = self.get_url_parametros()
        indice_inicio = url_parametros.find(parametro_busca) + len(parametro_busca) + 1
        indice_e_comercial = url_parametros.find('&', indice_inicio)
        if indice_e_comercial == -1:
            return url_parametros[indice_inicio:]
        else:
            return url_parametros[indice_inicio:indice_e_comercial]

    def conversor(self):
        valor = int(self.get_valor_parametro('quantidade'))
        moeda_origem = self.get_valor_parametro('moedaOrigem')
        moeda_destino = self.get_valor_parametro('moedaDestino')
        cambio = __class__.valores_moedas[moeda_origem] / __class__.valores_moedas[moeda_destino]
        return valor / cambio

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return f'URL: {self.url}\nParâmetros: {self.get_url_parametros()}\nBase: {self.get_url_base()}'

url = 'https://www.bytebank.com.br/cambio?moedaOrigem=real&moedaDestino=dolar_canadense&quantidade=100'
extrator_url = ExtratorURL(url)

print(extrator_url)
print(len(extrator_url))
print(extrator_url.get_valor_parametro('moedaOrigem'))
print(extrator_url.conversor())