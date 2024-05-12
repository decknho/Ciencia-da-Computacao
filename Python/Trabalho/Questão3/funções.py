import main


def escolha_servico(n):
    global servico
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
    servico = serv


def num_pagina(n):
    num = input(int('Numero de paginas (MAX 20.000)? '))
    while num <= 0 or n > 20000:
        print('O que você digitou é menor do que 1 ou maior que 20.000 ou não é um valor numérico!!')
        num = input(int('Digite novamente: '))


"""def servico_extra():"""