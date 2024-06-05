import pymssql

def InsertIntoTable(server, user, password, database, table, columns, data):
    """
    Insere dados em uma tabela especificada no banco de dados.

    Args:
    server (str): Endereço do servidor SQL.
    user (str): Usuário para autenticação no SQL Server.
    password (str): Senha para autenticação no SQL Server.
    database (str): Nome do banco de dados.
    table (str): Nome da tabela onde os dados serão inseridos.
    columns (tuple): Tupla contendo os nomes das colunas.
    data (tuple): Tupla contendo os dados a serem inseridos.

    Returns:
    None
    """
    try:
        # Estabeleça a conexão
        conn = pymssql.connect(server=server, user=user, password=password, database=database)
        cursor = conn.cursor()

        # Comando SQL para inserir dados
        placeholders = ', '.join(['%s'] * len(data))
        columns_str = ', '.join(columns)
        insert_query = f"INSERT INTO {table} ({columns_str}) VALUES ({placeholders})"
        
        # Executa o comando de inserção
        cursor.execute(insert_query, data)
        
        # Confirma a transação
        conn.commit()

        print("Dados inseridos com sucesso!")
    except pymssql.OperationalError as e:
        print(f"Erro operacional: {e}")
    except pymssql.InterfaceError as e:
        print(f"Erro de interface: {e}")
    except Exception as e:
        print(f"Outro erro ocorreu: {e}")
    finally:
        # Fecha a conexão
        if 'conn' in locals():
            conn.close()
