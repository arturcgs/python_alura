import re

padrao_celular = re.compile('(\+?\(?[0-9]{2,3}\)?)?(\(?[0-9]{2}\)?)([0-9]{5}-?[0-9]{4})')
padrao_telefone_fixo = re.compile('(\+?\(?[0-9]{2,3}\)?)?(\(?[0-9]{2}\)?)([0-9]{4}-?[0-9]{4})')
texto = '5511964922298'

padrao1 = '\(?[0-9]\)?'
texto1 = '(8)95623'

resposta = re.findall(padrao_celular, texto)
resposta2 = re.findall(padrao_telefone_fixo, texto)
busca = padrao_celular.search(texto)
print(busca.group())

print(resposta)
print(resposta2)
print(bool([]))