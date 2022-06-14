def jogar():
    print('\n' + "*" * 27 + "\nBem vindo ao jogo da Forca!\n" + "*" * 27)

    #importando lista de palavras
    palavras = []
    with open("palavras.txt", encoding='UTF-8') as arquivo:
        palavras = [linha.strip() for linha in arquivo]





if __name__ == '__main__':
    jogar()
