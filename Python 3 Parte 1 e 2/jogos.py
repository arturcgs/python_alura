import adivinhacao
import forca

print('*' * 10 + '\nBem vindo!\n' + '*' * 10)
print('\nOpções de jogos: \n(1) Adivinhação\n(2) Forca\n(0) Sair')

while True:
    jogo = int(input('\nQual jogo você deseja jogar? '))
    if jogo == 1:
        adivinhacao.jogar()
    elif jogo == 2:
        forca.jogar()
    elif jogo == 0:
        print('Volte sempre!')
        break
