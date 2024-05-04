print('Bem-vindo(a) a loja do Dereck Eder')

valor_total = 0
escolhas = ''

"""Cardápio"""

while True:
    """Mensagem de erro em caso de sabor invalido"""
    sabor = input(str('Escolha o sabor (CP/AC): ')).upper()
    sabores = ''
    while True:
        if sabor == str('AC') or sabor == str('CP'):
            break
        else:
            print('Sabor inválido')
            sabor = input(str('Escolha o sabor (CP/AC): ')).upper()

    """Mensagem de erro em caso de tamanho invalido"""
    tamanho = input(str('Escolha o tamanho (P/M/G): ')).upper()
    while True:
        if tamanho == str('P') or tamanho == str('M') or tamanho == str('G'):
            break
        else:
            print('Tamanho inválido')
            tamanho = input(str('Escolha o tamanho (P/M/G): ')).upper()
    

    if sabor == str('AC') and tamanho == str ('P'):
        sabor_ = 'Açai'
        valor = 11
        valor_total = valor_total + valor
    elif sabor == str ('AC') and tamanho == str ('M'):
        sabor_ = 'Açai'
        valor = 15
        valor_total = valor_total + valor
    elif sabor == str ('AC') and tamanho == str ('G'):
        sabor_ = 'Açai'
        valor = 20
        valor_total = valor_total + valor
    elif sabor == str('CP') and tamanho == str ('P'):
        sabor_ = 'Cupuaçu'
        valor = 9
        valor_total = valor_total + valor
    elif sabor == str ('CP') and tamanho == str ('M'):
        sabor_ = 'Cupuaçu'
        valor = 14
        valor_total = valor_total + valor
    else:
        sabor_ = 'Cupuaçu'
        valor = 18
        valor_total = valor_total + valor
    escolhas = escolhas + f'  Um {sabor_} do tamanho {tamanho}: R${valor}\n'
    sabores = input(str('Mais algum pedido? (S/N); ')).upper()
    if sabores != str('N'):
        continue
    else:
        break

print('Você pediu:')
print(escolhas)
print(f'O valor total a ser pago: R${valor_total}')
