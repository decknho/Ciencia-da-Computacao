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
    num = int(input('Numero de paginas (MAX 20.000)? '))
    while num <= 0 or num > 20000:
        print('O que você digitou é menor do que 1 ou maior que 20.000 ou não é um valor numérico!!')
        num = int(input('Digite novamente: '))
    return num


"""def servico_extra():"""