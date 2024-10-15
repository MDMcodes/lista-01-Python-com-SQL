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

# #DELETE
def deletar_na_tabela():
    id_input = int(input('Digite o ID do carro que deseja deletar: '))
    comando_sql = f'DELETE FROM produtos WHERE idprodutos = {id_input}'
    cursor.execute(comando_sql)
    conexao_banco.commit()
#SEARCH
def buscar_na_tabela():
    print('Pesquisar por: ')
    print('ID = 1')
    print('MARCA = 2')
    print('MODELO = 3')
    opc = int(input(f"Selecione sua opção: "))
    if opc == 1:
        id_input = int(input('Digite o ID do carro a ser pesquisado: '))
        comando_sql = 'SELECT * FROM produtos WHERE idprodutos = %s'
        cursor.execute(comando_sql, (id_input,))
        #DADOS_TABELA É A LISTA CONTENDO TODAS AS INFORMAÇOES DO CARRO Q POSSUI ID PASSANDO NO SELECT
        dados_tabela = cursor.fetchall()
        for dado in dados_tabela:
            print(dado)
    elif opc == 2:
        marca_input = input("Digite a marca do carro a ser pesquisado: ")
        comando_sql = 'SELECT * FROM produtos WHERE marca = %s'
        cursor.execute(comando_sql, (marca_input,))
        dados_tabela = cursor.fetchall()
        for dado in dados_tabela:
            print(dado)
    elif opc == 3:
        modelo_input = input('Digite o modelo do carro a ser pesquisado: ')
        comando_sql = 'SELECT * FROM produtos WHERE modelo = %s'
        cursor.execute(comando_sql, (modelo_input,))
        dados_tabela = cursor.fetchall()
        for dado in dados_tabela:
            print(dado)
    else:
        print('Opção inválida')
        buscar_na_tabela()
        conexao_banco.commit()


while True:
    print('SELECIONE A OPÇÃO DESEJADA: ')
    print('1 - CADASTRAR CARRO')
    print('2 - PESQUISAR CARROS')
    print('3 - DELETAR CARRO')
    print('4 - SAIR')
    opc = int(input(f"Selecione sua opção: "))
    if opc == 1:
        criar_na_tabela()
    elif opc == 2:
        buscar_na_tabela()
    elif opc == 3:
        deletar_na_tabela()
    elif opc == 4:
        print('Encerrando programa....')
        break
    else:
        print('Opção inválida')  




