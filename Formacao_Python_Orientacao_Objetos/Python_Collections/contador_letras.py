from textos import texto1, texto2
from collections import Counter

def analisa_frequencia_letras(texto):
    aparicoes = Counter(texto.lower())
    total_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, frequencia / total_caracteres) for letra, frequencia in aparicoes.items()]
    mais_comum = Counter(dict(proporcoes)).most_common(10)
    for caractere, frequencia in mais_comum:
        print(f'{caractere} ==> {frequencia:.2f}%')

print('Frequência de palavras no texto 1:')
analisa_frequencia_letras(texto1)
print('-'*10)
print('Frequência de palavras no texto 2:')
analisa_frequencia_letras(texto2)