import mysql.connector

conexao_banco = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='reservaex04'
)

cursor = conexao_banco.cursor()

#SISTEMA DE RESERVAS

def cadastrar_reserva():
    id_input = int(input('Digite o ID da reserva: '))
    nome_input = input('Digite o nome do cliente: ')
    quarto_input = input('Digite o quarto a ser reservado: ')
    data_checkin_input = input('Digite a data de check-in: ')
    data_checkout_input = input('Digite a data de check-out: ')
                                                                              #NOME DA COLUNA NO SQL
    comando_sql = f"SELECT * FROM reservas WHERE quarto = '{quarto_input}' AND (data_checkin BETWEEN '{data_checkin_input}' AND '{data_checkout_input}' OR data_checkout BETWEEN '{data_checkin_input}' AND '{data_checkout_input}')"
    cursor.execute(comando_sql)
    dados_tabela = cursor.fetchall()
    if dados_tabela:
        print('Quarto indisponivel')
    else:
        comando_sql = f"INSERT INTO reservas (ID, nome_cliente, quarto, data_checkin, data_checkout) VALUES ({id_input}, '{nome_input}', '{quarto_input}', '{data_checkin_input}', '{data_checkout_input}')"
        cursor.execute(comando_sql)
        conexao_banco.commit()

# (data_checkin BETWEEN '{data_checkin_input}' AND '{data_checkout_input}' OR data_checkout BETWEEN '{data_checkin_input}' AND '{data_checkout_input}'): Essa parte do comando é um pouco mais complexa. Ela verifica se a data de check-in ou a data de check-out está dentro do intervalo de datas digitado pelo usuário.

# BETWEEN: é um operador que verifica se um valor está dentro de um intervalo.

def alterar_data():
    id_input = int(input('Digite o ID da reserva: '))
    comando_sql = f'SELECT * FROM reservas WHERE ID = {id_input}'
    cursor.execute(comando_sql)
    dados_tabela = cursor.fetchall
    if dados_tabela:
        data_checkin_input = input('Digite a nova data de check-in: ')
        data_checkout_input = input('Digite a nova data de check-out')
        comando_sql = f'UPDATE reservas SET data_checkin = "{data_checkin_input}" AND SET data_checkout = "{data_checkout_input}"'