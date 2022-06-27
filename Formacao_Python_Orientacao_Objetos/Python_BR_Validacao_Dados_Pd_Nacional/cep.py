import requests
import re

class Cep:

    def __init__(self, cep):
        cep = self.limpeza_cep(cep)
        if self.verifica_cep(cep):
            self.cep = cep

    #métodos especiais
    def __str__(self):
        endereco = self.pega_endereco_cep()
        return f"{endereco['logradouro']}, {endereco['bairro']}, {endereco['localidade']} - {endereco['uf']}, {endereco['cep']}"

    #funções pra incialização (limpeza e verificação)
    def limpeza_cep(self, cep):
        cep = str(cep).strip()
        if '-' in cep:
            cep = cep.replace('-', '')
        return cep

    def verifica_cep(self, cep):
        padrao_cep = re.compile('[0-9]{8}')
        match = padrao_cep.match(cep)
        if match:
            return True
        else:
            raise ValueError('Valor Inválido')

    #funções pra API do CEP
    def pega_endereco_cep(self):
        endereco_API = f'https://viacep.com.br/ws/{self.cep}/json/'
        r = requests.get(endereco_API)
        return r.json()


