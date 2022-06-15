import random
import sprites

def jogar():
    print('*' * 27 + '\nBem vindo ao jogo da Forca!\n' + '*' * 27 + '\n')

    #importando lista de palavras
    palavras = []
    with open("palavras.txt", encoding='UTF-8') as arquivo:
        palavras = [linha.strip() for linha in arquivo]

    #selecionando palavra aleatório da lista
    palavra_secreta = palavras[random.randint(0, len(palavras) - 1)]

    lista_chute = []
    lista_index = []
    erros = 0

    #variáveis pra imprimir braço e perna aleatório
    braco_aleatorio = random.randint(20, 21)
    perna_aleatorio = random.randint(40, 41)

    #mensagem inicial
    print('Palavra secreta:\n' + "_ " * len(palavra_secreta))

    while True:
        #imprimindo forca
        if erros == 2:
            print(sprites.forca[braco_aleatorio])
        elif erros == 4:
            print(sprites.forca[perna_aleatorio])
        else:
            print(sprites.forca[erros])

        chute = input('Escolha uma letra: ').strip().lower()
        lista_chute.append(chute)

        index = 0 #setando variável index

        #letra certa
        if chute in palavra_secreta:
            for letra in palavra_secreta: #iterando as letras da palavra
                if chute == letra:
                    lista_index.append(index)
                index += 1
        #letra errada
        else:
            erros += 1
            print(f'Essa letra não está na palavra\nVc usou {erros} de 6 erros')

        #check derrota
        if erros == 5:
            print(sprites.forca[5])
            print(f'Vc perdeu!\nA palavra era {palavra_secreta}')
            break

        #check vitória
        if len(lista_index) == len(palavra_secreta):
            print(palavra_secreta)
            print('Parabéns! Vc achou a palavra secreta!')
            break

        #imprimindo palavra
        for i in range(0, len(palavra_secreta.capitalize())):
            if i in lista_index:
                print(f"{palavra_secreta[i]} ", end='')
            else:
                print("_ ", end='')
        print()

if __name__ == '__main__':
    jogar()