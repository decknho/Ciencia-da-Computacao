print('Bem-vindo(a) a loja do Dereck Eder')

valor_total = 0

"""Cardápio"""


"""Mensagem de erro em caso de sabor invalido"""
sabor = input('Escolha o sabor (CP/AC) :').upper
while ('AC, CP') not in sabor:
    print('Sabor invalido. selecione novamente!')
    sabor = input('Escolha o sabor (CP/AC) :').upper


"""Mensagem de erro em caso de tamanho invalido"""