import funções

print('Boas vindas á copiadora do Dereck')
print('Entre com o serviço desejado:\n'
      '  Digitalização (DIG)\n'
      '  Impressão Colorida (ICO)\n'
      '  Impressão Preto e Branco (IPB)\n'
      '  Fotocópia (FOT)') #

servico_valor = 0
servico = funções.escolha_servico() #opções de escolha do serviço desejado do usuario e seu respectivo valor o salvando numa variavel
if servico == str('DIG'):
    servico_valor = float(1.10)
elif servico == str('ICO'):
    servico_valor = float(1.0)
elif servico == str('IPB'):
    servico_valor = float(0,40)
elif servico == str('FOT'):
    servico_valor = float(0,20)
paginas = funções.num_pagina() # quantidade de paginas desejadas pelo usuario e salvas numa variavel

desc = 0
if paginas >= 20 and paginas < 200:
    desc = 15
if paginas >= 20 and paginas < 200:
    desc = 20
if paginas >= 20 and paginas < 200:
    desc = 25

total = (servico_valor * paginas) #calculando total sem desconto
valor_com_desconto = total - (total / 100 * desc)
print(f'O valor do serviço sem desconto é R${total: .2f}')
if paginas < 20:
    print('Numero de paginas insuficientes para receber desonto logo o valor continua o mesmo!')
else:
    print(f'Você recebeu um desconto de {desc}% pela quantidade de {paginas} paginas, seu novo valor é R${valor_com_desconto: .2f}')

extra = funções.servico_extra()

if extra == 15 or extra == 40:
      print('Você selecionou um serviço extra!')
      if extra == 15:
          print(f'O novo valor total é {valor_com_desconto + extra: .2f}')
      elif extra == 40:
          print(f'O novo valor total é {valor_com_desconto + extra: .2f}')
else:
    print('Você optou por não acresentar um serviço extra!')