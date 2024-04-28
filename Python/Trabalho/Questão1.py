print('Bem-vindo(a) a loja do Dereck Eder')

""""Variaveis para coletar preços e quantidade de protuto"""
valor_do_produto = int(input('Valor do produto? '))
quantidade = int(input('Quantidade desejada?'))
preço_total = valor_do_produto * quantidade

"""print sobre a quantidade e valor do produto"""
print(f'Valor do produto: {valor_do_produto}')
print(f'Quantidade escolhida: {quantidade}')

"""Resultados do valor com desconto baseado no preço"""
if preço_total < 2500:
    print(f'O valor total deu R${preço_total}, sendo assim sem possibilidade de desconto!')
elif preço_total >= 2500 and preço_total < 6000:
    desconto = preço_total - (preço_total / 100 * 4)
    print(f'Sua compra deu um valor total de R${preço_total}, tendo um desconto de 4% seu novo preço sera de {desconto}')
elif preço_total >= 6000 and preço_total < 10000:
    desconto = preço_total - (preço_total / 100 * 7)
    print(f'Sua compra deu um valor total de R${preço_total}, tendo um desconto de 7% seu novo preço sera de {desconto}')
else:
    desconto = preço_total - (preço_total / 100 * 11)
    print(f'Sua compra deu um valor total de R${preço_total}, tendo um desconto de 11% seu novo preço sera de {desconto}')