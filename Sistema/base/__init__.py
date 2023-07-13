def leitura():
    import menu
    menu.escreva('         PESSOAS CADASTRADAS     ')
    with open('C:\\Users\\Ageri\\Desktop\\SCRIPTS\\Python\\cadastro\\base\\base.txt', "r+") as arquivo:
        print(arquivo.read())

