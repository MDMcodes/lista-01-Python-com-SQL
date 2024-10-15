import mysql.connector

conexao_banco = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='inventarioex3'
)

cursor = conexao_banco.cursor()

def criar_na_tabela():
    id_input = int(input('Digite o ID do novo produto: '))
    nome_input = input('Digite o nome do produto: ')
    categoria_input = input('Digite a cateoria do novo produto: ')
    quantidade_input = int(input('Digite a quantidade do produto: '))
    comando_sql = f'SELECT * FROM produtos WHERE nome = "{nome_input}" AND  categoria = "{categoria_input}"'
    cursor.execute(comando_sql)
    dados_tabela = cursor.fetchall()
    if dados_tabela:
        print('Produto já existe na tabela')
    else:
        comando_sql = f'INSERT INTO produtos  (ID, nome, categoria, quantidade) VALUES ({id_input}, "{nome_input}", "{categoria_input}", {quantidade_input})'
        cursor.execute(comando_sql)
        conexao_banco.commit()
        print('Produto adicionado com sucesso')

def alterar_na_tabela():
    id_input = int(input('Digite o ID do produto a ter a quantidade alterada: '))
    comando_sql = f'SELECT * FROM produtos WHERE ID = {id_input}'
    cursor.execute(comando_sql)
    dados_tabela = cursor.fetchall()
    if dados_tabela:
        quantidade_input = int(input('Digite a quantidade nova do produto: '))
        comando_sql = f'UPDATE produtos SET quantidade = {quantidade_input} WHERE ID = {id_input}'
        cursor.execute(comando_sql)
        conexao_banco.commit()
        print('Quantidade alterada com sucesso')
    else:
        print('Produto não encontrado')

def deletar_na_tabela():
    id_input = int(input('Digite o ID do produto a ser deletado: '))
    comando_sql = f'SELECT * FROM produtos WHERE ID = {id_input}'
    cursor.execute(comando_sql)
    dados_tabela = cursor.fetchall()
    if dados_tabela:
        comando_sql = f'DELETE FROM produtos WHERE ID = {id_input}'
        cursor.execute(comando_sql)
        conexao_banco.commit()
        print('Produto deletado com sucesso')
    else:
        print('Produto não encontrado')

def visualizar_na_tabela():
        comando_sql = f'SELECT * FROM produtos'
        cursor.execute(comando_sql)
        dados_tabela = cursor.fetchall()
        for dado in dados_tabela:
            print(f'ID: {dado[0]} - NOME: {dado[1]} -  CATEGORIA: {dado[2]}  - QUANTIDADE: {dado[3]}')

while True:
    print('1 - Inserir produto')
    print('2 - Alterar produto')
    print('3 - Deletar produto')
    print('4 - Visualizar produtos')
    print('5 - Sair')
    opcao = input('Digite a opção desejada: ')
    if opcao == '1':
        criar_na_tabela()
    elif opcao == '2':
        alterar_na_tabela()
    elif opcao == '3':
        deletar_na_tabela()
    elif opcao == '4':
        visualizar_na_tabela()
    elif opcao == '5':
        print('Encerrando programa.....')
        break