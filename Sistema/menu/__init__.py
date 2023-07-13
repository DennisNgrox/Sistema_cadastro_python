def escreva(txt):
    print('-' * 36)
    print(txt)
    print('-' * 36)

def opcao():
    escreva('           MENU PRINCIPAL           ')

    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar nova Pessoa')
    print('3 - Sair do Sistema')
    print('------------------------------------')
    number = int(input('Sua Opção: '))
    
    if number == 1:
        from time import sleep
        import base
        base.leitura()
        sleep(3)
        opcao()
    elif number == 2:
        from time import sleep
        import registro
        escreva('           CADASTRAR           ')
        nome = str(input('Digite o nome que deseja cadastrar: '))
        idade = str(input(f'Digite a idade do(a) {nome}: '))
        registro.cadastrar(nome, idade)
        print(f'{nome} cadastrado com a idade {idade} no Sistema')
        sleep(3)
        opcao()

    elif number == 3:
        try:
            escreva('           FINALIZANDO           ')
            from time import sleep
            finalizar = 'Até maaais veeeerrr'
        finally:
            print(finalizar)
    else:
        from time import sleep
        print(f'Opção {number} não existe no Menu.')
        sleep(1)
        opcao()
