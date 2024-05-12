import funções

print('Boas vindas á copiadora do Dereck')
print('Entre com o serviço desejado:\n'
      '  Digitalização (DIG)\n'
      '  Impressão Colorida (ICO)\n'
      '  Impressão Preto e Branco (IPB)\n'
      '  Fotocópia (FOT)')

servico_valor = 0
servico = funções.escolha_servico()
if servico == str('DIG'):
    servico_valor = float(1.10)
elif servico == str('ICO'):
    servico_valor = float(1.0)
elif servico == str('IPB'):
    servico_valor = float(0,40)
elif servico == str('FOT'):
    servico_valor = float(0,20)
paginas = funções.num_pagina()

valor_paginas = (servico_valor * paginas)
print(f'O valor do serviço sem desconto é R${valor_paginas}')
if valor_paginas < 20:
    print('Numero de paginas insuficientes para receber desonto logo o valor continua o mesmo!')