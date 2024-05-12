import funções

print('Boas vindas á copiadora do Dereck')
print('Entre com o serviço desejado:\n'
      '  Digitalização (DIG)\n'
      '  Impressão Colorida (ICO)\n'
      '  Impressão Preto e Branco (IPB)\n'
      '  Fotocópia (FOT)')


servico = ''
paginas = 0
extra = 0

funções.escolha_servico()

print(servico)