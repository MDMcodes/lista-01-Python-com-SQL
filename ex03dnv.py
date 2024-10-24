import mysql.connector

conexao_banco = mysql.connector.connect(
    host ='127.0.0.1',
    user = 'root',
    password = '',
    database = 'revenda_carros'
)

cursor = conexao_banco.cursor

def inserir_na_tabela():
    id_input = int(input('Digite o ID: '))
    nome_input = input('Digite o nome: ')
    categoria_input = input('Digite a categoria: ')
    quantidade_input = int(input('Digite a quantidade:'))
    comando_sql = f'SELECT * FROM produtos'
    cursor.execute(comando_sql)
    dados_tabela = cursor.fetchall()
    if nome_input in dados_tabela[1] and categoria_input in dados_tabela[2]:
        print('produto já existe')
    else:
        comando_sql = f'INSERT INTO produtos (ID, nome, categoria, quantidade) VALUES ({id_input}, "{nome_input}", "{categoria_input}", {quantidade_input})'
        cursor.execute(comando_sql)
        conexao_banco.commit()
        print('Produto cadastrado')

def alterar_na_tabela():
    id_input = int(input('Digite o ID: ')) # 2
    comando_sql = f'SELECT * FROM produtos'
    cursor.execute(comando_sql)
    dados_tabela = cursor.fetchall()
    if id_input in dados_tabela[0]: #qual a condicao aq? o certo seria = if id_input in dados_tabela[0]
        quantidade_input = int(input('Digite a quantidade nova: '))
        comando_sql = f'UPDATE produtos SET quantidade = {quantidade_input} WHERE ID = {id_input}' # mudei aqui pq antes tava "{id_input}" como uma string e é int
        cursor.execute(comando_sql) 
        conexao_banco.commit()
        print('Quantidade alterada')
    else:
        print('ID não encontrado')

def deletar_na_tabela():
    id_input = int(input('Digite o id: '))
    comando_sql = f'SELECT * FROM produtos WHERE ID = {id_input}'
    cursor.execute(comando_sql)
    dados_tabela = cursor.fetchall()
    if len(dados_tabela) <= 0:
        comando_sql = f'DELETE FROM produtos WHERE ID = {id_input}'
        cursor.execute(comando_sql)
        conexao_banco.commit()
    else:
        ('ID nao existe')

def visualizar():
    comando_sql = f'SELECT * FROM produtos'
    cursor.execute(comando_sql)
    dados_tabela = cursor.fetchall()
    for dado in dados_tabela:
        print(f'ID = {dado[0]}\nNOME = {dado[1]}\nCATEGORIA = {dado[2]}\nQUANTIDADE = {dado[3]}')

while True:
    print('1 - Inserir produto')
    print('2 - Alterar produto')
    print('3 - Deletar produto')
    print('4 - Visualizar produtos')
    print('5 - Sair')
    opcao = input('Digite a opção desejada: ')
    if opcao == '1':
        inserir_na_tabela()
    elif opcao == '2':
        alterar_na_tabela()
    elif opcao == '3':
        deletar_na_tabela()
    elif opcao == '4':
        visualizar()
    elif opcao == '5':
        print('Encerrando programa.....')
        break