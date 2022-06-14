import random

def jogar():
    print("\n" + "*" * 31 + '\nBem Vindo ao Jogo de Advinhação\n' + '*' * 31) #bem bindo

    #seleção de dificuldade
    print('\nNíveis de dificuldade disponíveis:'
          '\n(1) Fácil\n(2) Médio\n(3) Difícil\n(0) Sair')
    dificuldade = int(input('Selecione a dificuldade: '))

    if dificuldade == 1:
        total_tentativas = 20
    elif dificuldade == 2:
        total_tentativas = 10
    elif dificuldade == 3:
        total_tentativas = 5
    elif dificuldade == 0:
        total_tentativas = 0
    else:
        print('Este não é um valor válido')

    #pontuação
    pontos = 1000

    #valor secreto
    valor_secreto = random.randint(1, 101)

    for i in range(0, total_tentativas):

        chute = int(input('\nDigite um número entre 1 e 100: '))

        #valores fora do permitido
        if chute > 100 or chute < 1:
            print('Valor inválido. Tente novamente')
            print(f'Vc tem {total_tentativas - (i + 1)} tentativas restantes')
            pontos = pontos - abs(chute - valor_secreto)
            continue

        #definindo maior, maior10, igual, menor10 e menor
        maior = chute > valor_secreto + 10
        maior10 = valor_secreto + 10 >= chute > valor_secreto
        igual = chute == valor_secreto
        menor10 = valor_secreto - 10 <= chute < valor_secreto
        menor = chute < valor_secreto - 10

        #informando localização do chute
        if maior:
            print('Vc chutou um valor muito alto')
        elif maior10:
            print('Vc chutou um valor um pouco mais alto')
        elif igual:
            print('Vc acertou!')
            print(f'Vc fez {pontos} pontos')
            break
        elif menor10:
            print('Vc chutou um valor um pouco mais baixo')
        elif menor:
            print('Vc chutou um valor muito baixo')

        #número de tentativas restantes
        print(f'Vc tem {total_tentativas - (i + 1)} tentativas restantes')

        #subtraindo pontos
        pontos = pontos - abs(chute - valor_secreto)

    print('Fim de jogo!')

if __name__ == '__main__':
    jogar()