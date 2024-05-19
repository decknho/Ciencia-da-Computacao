print('Boas vindas a livraria do Dereck Eder')

livros = [{'id' : 0, 'nome' : 'Deco', 'autor' : 'Amir', 'editora' : 'MM'},
          {'id' : 1, 'nome' : 'Eve', 'autor' : 'Satar', 'editora' : 'NN'},
          {'id' : 2, 'nome' : 'Tifa', 'autor' : 'Sanny', 'editora' : 'SS'},
          {'id' : 3, 'nome' : 'Amortizar', 'autor' : 'Amir', 'editora' : 'TT'},
          {'id' : 4, 'nome' : 'Potato', 'autor' : 'EU', 'editora' : 'MM'}]
id_global = 1
def cadastrar_livro(id):
    global id_global
    livro = {'id': [id_global], 'nome' : [], 'autor' : [], 'editora' : []}
    livro['nome'] = input('Nome do livro? ')
    livro['autor'] = input('Nome do autor? ')
    livro['editora'] = input('Nome da editora? ')
    livros.append(livro.copy())


"""def consultar_livro():"""


def remover_livro():
    apagar = int(input('Qual ID você deseja apagar? '))
    for item in livros:
        if item == apagar:
            livros.remove[apagar]

    

print('1 - Cadastrar livro\n'
      '2 - Consultar livro\n' 
      '3 - Remover livro\n'
      '4 - Sair do programa')

while True:
    servico = int(input('Você deseja? '))
    try:
        if servico >= 1 and servico <= 4:
            break
        else:
            print('Não existe essa opção!')
    except ValueError:
        print('Error, digite um numero!')

"""if servico == 1:
    cadastrar_livro(id_global)
    id_global =+ 1"""
if servico == 2:
    print('1 - Consultar todos\n'
        '2 - Consultar por id\n' 
        '3 - Consultar por autor\n'
        '4 - Voltar ao menu')
    while True:
        try:
            consulta = int(input('Você deseja? '))
            if consulta >= 1 and consulta <= 4:
                break
            else:
                print('Não existe essa opção!')
        except ValueError:
            print('Error, digite um numero!')
    if consulta == 1:
        for livraria in livros:
            for chave, valor in livraria.items():
                print(f'{chave}: {valor}')
            print()  
    if consulta == 2:
        while True:
            livro_id = ''
            try:
                livro_id = int(input('Qual o id do livro? '))
                break
            except ValueError:
                print('Digite um ID valido!')
        for item in livros:
            num = item['id']
            if int(num) == int(livro_id):
                print(f"ID: {item['id']}")
                print(f"NOME: {item['nome']}")
                print(f"AUTOR: {item['autor']}")
                print(f"EDITORA: {item['editora']}")
    if consulta == 3:
        autor = str(input('Nome do autor? ')).upper()
        for item in livros:
            copia = item['autor']
            if str(copia).upper() == str(autor).upper():
                print(f"ID: {item['id']}")
                print(f"NOME: {item['nome']}")
                print(f"AUTOR: {item['autor']}")
                print(f"EDITORA: {item['editora']}")

    