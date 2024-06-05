import pymssql

def SelectFromTable(server, user, password, database, table, columns='*'):
    """
    Seleciona dados de uma tabela especificada no banco de dados.

    Args:
    server (str): Endereço do servidor SQL.
    user (str): Usuário para autenticação no SQL Server.
    password (str): Senha para autenticação no SQL Server.
    database (str): Nome do banco de dados.
    table (str): Nome da tabela de onde os dados serão selecionados.
    columns (str): Colunas a serem selecionadas, por padrão todas as colunas ('*').

    Returns:
    list: Lista de tuplas contendo os registros selecionados.
    """
    try:
        # Estabeleça a conexão
        conn = pymssql.connect(server=server, user=user, password=password, database=database)
        cursor = conn.cursor()

        # Comando SQL para selecionar dados
        select_query = f"SELECT {columns} FROM {table}"
        
        # Executa o comando de seleção
        cursor.execute(select_query)
        
        # Obtém todos os registros
        results = cursor.fetchall()

        return results
    except pymssql.OperationalError as e:
        print(f"Erro operacional: {e}")
    except pymssql.InterfaceError as e:
        print(f"Erro de interface: {e}")
    except Exception as e:
        print(f"Outro erro ocorreu: {e}")
        return []
    finally:
        # Fecha a conexão
        if 'conn' in locals():
            conn.close()