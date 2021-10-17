import sqlite3


def init_airtrans_db(connection, cursor):
    with open('sql/INIT_DB.sql') as initial_sql_script_fin:
        init_db_script = initial_sql_script_fin.read().strip()
        cursor.executescript(init_db_script)
        connection.commit()


def run_query(cursor, sql_query):
    cursor.execute(sql_query)
    columns = [description[0] for description in cursor.description]
    rows = cursor.fetchall()
    return {
        'columns': columns,
        'rows': [list(row) for row in rows]
    }


def test_query():
    connection = sqlite3.connect(':memory:')
    cursor = connection.cursor()
    init_airtrans_db(connection, cursor)

    # место для запуска SQL запросов
    with open('sql/test.sql') as sql_query_fin:
        sql_query = sql_query_fin.read().strip()
    query_result = run_query(cursor, sql_query)

    print('Имена столбцов в SQL-запросе:')
    print(*query_result['columns'], sep=',')
    print()
    print('Результат SQL-запроса:')
    for row in query_result['rows']:
        print(*row, sep=',')


if __name__ == '__main__':
    try:
        test_query()
    except Exception as e:
        print('Возникла ошибка:')
        print(e)
