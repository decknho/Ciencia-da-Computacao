print('Boas vindas a livraria do Dereck Eder')

livros = []
id_global = 0
def cadastrar_livro(id):
    global id_global
    livro = {'id': [id_global], 'nome' : [], 'autor' : [], 'editora' : []}
    livro['nome'] = input('Nome do livro? ')
    livro['autor'] = input('Nome do autor? ')
    livro['editora'] = input('Nome da editora? ')
    livros.append(livro)
    

print('1 - Cadastrar livro\n'
      '2 - Consultar livro\n' 
      '3 - Remover livro\n'
      '4 - Sair do programa')

while True:
    try:
        servico = int(input('Você deseja? '))
        if servico >= 1 and servico <= 4:
            break
        else:
            print('Não existe essa opção!')
    except ValueError:
        print('Error, digite um numero!')

if servico == 1:
    cadastrar_livro(id_global)

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

    