print('Boas vindas a livraria do Dereck Eder')

livros = []
id_global = 0
def cadastrar_livro():
    global id_global
    id_global += 1
    livro = {'id': [], 'nome' : [], 'autor' : [], 'editora' : []}
    livro['id'] = id_global
    livro['nome'] = input('Nome do livro? ')
    livro['autor'] = input('Nome do autor? ')
    livro['editora'] = input('Nome da editora? ')
    livros.append(livro.copy())
    livro.clear()


def consultar_livro(n):
        consulta = n
        if consulta == 1: # consulta todos os livros
            for livraria in livros:
                for chave, valor in livraria.items():
                    print(f'{chave}: {valor}')
                print()

        if consulta == 2: # consulda o livro pelo id
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
                    print() # print vazio pra deixa a saida bonita

        if consulta == 3: # consulta pelo nome do autor
            autor = str(input('Nome do autor? ')).upper()
            for item in livros:
                copia = item['autor']
                if str(copia).upper() == str(autor).upper():
                    print(f"ID: {item['id']}")
                    print(f"NOME: {item['nome']}")
                    print(f"AUTOR: {item['autor']}")
                    print(f"EDITORA: {item['editora']}")
                    print() # print vazio pra deixa a saida bonita


def remover_livro():
    total_de_livros = len(livros)
    apagar = int(input('Qual ID você deseja apagar? '))
    while apagar < 0 or apagar > total_de_livros:
        print('ID Inválido')
        apagar = int(input('Qual ID você deseja apagar? '))
    for item in livros:
        if item['id'] == apagar:
            del livros[apagar - 1]
            print('Livro apagado com sucesso!')
            print(f" ID: {item['id']}")
            print(f" NOME: {item['nome']}")
            print(f" AUTOR: {item['autor']}")
            print(f" EDITORA: {item['editora']}")
            print() # print vazio pra deixa a saida bonita

print('1 - Cadastrar livro\n'
          '2 - Consultar livro\n' 
          '3 - Remover livro\n'
          '4 - Sair do programa')
print()
while True:
    while True:
        try:
            servico = int(input('Você deseja qual serviço? '))
            if servico >= 1 and servico <= 4:
                break
            else:
                print('Não existe essa opção!')
        except ValueError:
            print('Error, digite um numero!')

    if servico == 1: # condição para chamar a função "cadastra livro"
        cadastrar_livro()

    if servico == 2: # condição para chamar a função "consultar livro"
        print('1 - Consultar todos\n'
              '2 - Consultar por id\n' 
              '3 - Consultar por autor\n'
              '4 - Voltar ao menu')
        print()
        while True:
            try:
                consulta = int(input('Você deseja consultar por? '))
                if consulta >= 1 and consulta <= 4:
                    break
                else:
                    print('Não existe essa opção!')
            except ValueError:
                print('Error, digite um numero!')
        if consulta >= 1 and consulta < 4:
            consultar_livro(consulta)

    if servico == 3: # condição para chamar a função "remover livro"
        remover_livro()

    if servico == 4: # encerrar o programa
        print('PROGRAMA ENCERRADO!!')
        break