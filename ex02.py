import mysql.connector

conexao_banco = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='gerenciamentofunc'
)

cursor = conexao_banco.cursor()


def criar_na_tabela():
    id_input = int(input('Digite o ID do novo funcionário: '))
    nome_input = input('Digite o nome do novo funcionário: ')
    cargo_input = input('Digite o cargo do novo funcionário: ')
    comando_sql = f'SELECT * FROM funcionario WHERE ID = {id_input}'
    cursor.execute(comando_sql)
    dados_tabela = cursor.fetchall()
    if dados_tabela:  # Verifica se a lista não está vazia
        print('ID já existe')
    else:
        comando_sql = f'INSERT INTO funcionario (id, nome, cargo) VALUES ({id_input}, "{nome_input}", "{cargo_input}")'
        cursor.execute(comando_sql)
        conexao_banco.commit()
        print('Funcionário adicionado com sucesso')

def alterar_na_tabela():
    id_input = int(input('Digite o ID do funcionário que deseja alterar: '))
    comando_sql = f'SELECT * FROM funcionario WHERE ID = {id_input}'
    cursor.execute(comando_sql)
    dados_tabela = cursor.fetchall()
    if dados_tabela:  # Verifica se a lista não está vazia
        cargo_input = input('Digite o novo cargo do funcionário: ')
        comando_sql = f'UPDATE funcionario SET cargo = "{cargo_input}" WHERE ID = {id_input}'
        cursor.execute(comando_sql)
        conexao_banco.commit()
        print('Cargo alterado com sucesso')
    else:
        print('ID não existe')

def deletar_na_tabela():
    id_input = int(input('Digite o ID do funcionário que deseja deletar: '))
    comando_sql = f'SELECT * FROM funcionario WHERE ID = {id_input}'
    cursor.execute(comando_sql)
    dados_tabela = cursor.fetchall()
    if dados_tabela:  # Verifica se a lista não está vazia
        comando_sql = f'DELETE FROM funcionario WHERE ID = {id_input}'
        cursor.execute(comando_sql)
        conexao_banco.commit()
        print('Funcionário deletado com sucesso')
    else:
        print('ID não existe')

def pesquisar_na_tabela():
    print('Pesquisar por: ')
    print('ID = 1')
    print('NOME = 2')
    print('CARGO = 3')
    opc = int(input(f"Selecione sua opção: "))
    if opc == 1:
        id_input = int(input('Digite o ID do funcionario a ser pesquisado: '))
        comando_sql = f'SELECT * FROM funcionario WHERE ID = {id_input}'
        cursor.execute(comando_sql)
        dados_tabela = cursor.fetchall()
        for dado in dados_tabela:
            print(f'ID: {dado[0]} - NOME: {dado[1]} -  CARGO: {dado[2]}')
    elif opc == 2:
        nome_input = int(input('Digite o nome do funcionario a ser pesquisado: '))
        comando_sql = f'SELECT * FROM funcionario WHERE ID = {nome_input}'
        cursor.execute(comando_sql)
        dados_tabela = cursor.fetchall()
        for dado in dados_tabela:
            print(f'ID: {dado[0]} - NOME: {dado[1]} -  CARGO: {dado[2]}')
    elif  opc == 3:
        cargo_input = int(input('Digite o nome do funcionario a ser pesquisado: '))
        comando_sql = f'SELECT * FROM funcionario WHERE ID = {cargo_input}'
        cursor.execute(comando_sql)
        dados_tabela = cursor.fetchall()
        for dado in dados_tabela:
            print(f'ID: {dado[0]} - NOME: {dado[1]} -  CARGO: {dado[2]}')

while True:
    print('Menu: ')
    print('1 - Inserir funcionário')
    print('2 - Alterar cargo de funcionário')
    print('3 - Deletar funcionário')
    print('4 - Pesquisar funcionário')
    print('5 - Sair')
    opc = int(input(f"Selecione sua opção: "))
    if opc == 1:
        criar_na_tabela()
    elif opc == 2:
        alterar_na_tabela()
    elif opc == 3:
        deletar_na_tabela()
    elif opc == 4:
        pesquisar_na_tabela()
    elif opc == 5:
        print('Fechando o programa....')
        break



