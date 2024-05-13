def escolha_servico():
    serv = input(str('Qual é o serviço desejado? ')).upper()
    while True:
        if serv == str('DIG') or serv == str('ICO') or serv == str('IPB') or serv == str('FOT'):
                break
        print('Serviço não encontrado...')
        serv = input(str('Digite novamente o serviço desejado? ')).upper()
    if serv == str('DIG'):
        print('Você escolheu Digitalização, tendo o valor R$1,10 por pagina!')
    if serv == str('ICO'):
        print('Você escolheu Impressão Colorida, tendo o valor R$1,00 por pagina!')
    if serv == str('IPB'):
        print('Você escolheu Impressão Preto e Branco, tendo o valor R$0,40 por pagina!')
    if serv == str('FOT'):
        print('Você escolheu Fotocópia, tendo o valor R$0,20 por pagina!')
    return serv


def num_pagina():
    while True:
        try:
            num = int(input('Numero de paginas (MAX 20.000)? '))
            break
        except ValueError:
            print('Error! Digite somente numeros: ')
            continue
    while num <= 0 or num > 20000:
        print('O que você digitou é menor do que 1 ou maior que 20.000!!')
        num = int(input('Digite novamente: '))
    return num


def servico_extra():
    extra = int(input('Você deseja um serviço extra?\n'
                      '[ 1 ] Encadernação simples R$15\n'
                      '[ 2 ] Encadernação de capa dura R$40\n'
                      '[ 0 ] Não\n'))
    while True:
        if extra == 0 or extra == 1 or extra == 2:
            break
        extra = int(input('Erro! Digite uma opção valida: '))
    if extra == 1:
        return 15
    elif extra == 2:
        return 40
    else:
        return 0