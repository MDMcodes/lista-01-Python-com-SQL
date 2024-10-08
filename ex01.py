import mysql.connector

conexao_banco = mysql.connector.connect(
    host ='127.0.0.1',
    user = 'root',
    password = '',
    database = 'revenda_carros'
)

cursor = conexao_banco.cursor()

#CREATE
def criar_na_tabela():
    id_input = int(input('Digite o ID do novo carro: '))
    marca_input = input('Digite a marca do carro: ')
    modelo_input = input('Digite o modelo do carro: ')
    ano_input = int(input('Digite o ano do carro: '))
    cor_input = input('Digite a cor do carro: ')

    comando_sql = f'INSERT INTO produtos (idprodutos, marca, modelo, ano, cor) VALUES ({id_input}, "{marca_input}", "{modelo_input}",  {ano_input}, "{cor_input}")'


    cursor.execute(comando_sql)
    conexao_banco.commit()

#DELETE
def deletar_na_tabela():
    id_input = int(input('Digite o ID do carro a ser deletado: '))
    comando_sql = 'SELECT * FROM produtos'
    cursor.execute(comando_sql)
    dados_tabela = cursor.fetchall()
    for dado in dados_tabela:
        if dado[0] == id_input:
            comando_sql = f'DELETE FROM produtos WHERE idprodutos = {id_input}'
            cursor.execute(comando_sql)
            conexao_banco.commit()
            print(f'O carro foi deletado com sucesso')
            break
        else:
            print('Não encontrado')
            break

#SEARCH
def buscar_na_tabela():
    print('Pesquisar por: ')
    print('ID = 1')
    print('MARCA = 2')
    print('MODELO = 3')
    print('ANO = 4')
    opc = int(input()