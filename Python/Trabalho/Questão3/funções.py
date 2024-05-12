def escolha_servico():
    serv = input(str('Qual é o serviço desejado? ')).upper()
    while serv != str('DIG') or serv != str('ICO') or serv != str('IPB') or serv != str('FOT'):
        serv = input(str('Serviço não encontrado, digite novamente o serviço desejado? ')).upper()
    if serv == str('DIG'):
        print('Você escolheu Digitalização, tendo o valor R$1,10 por pagina!')
    if serv == str('ICO'):
        print('Você escolheu Impressão Colorida, tendo o valor R$1,00 por pagina!')
    if serv == str('IPB'):
        print('Você escolheu Impressão Preto e Branco, tendo o valor R$0,40 por pagina!')
    if serv == str('FOT'):
        print('Você escolheu Fotocópia, tendo o valor R$0,20 por pagina!')
    return serv

'''
def num_pagina():
'''