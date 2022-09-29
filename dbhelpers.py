def just_connect():
    import dbcreds
    import mariadb

    conn = mariadb.connect(
    user=dbcreds.user, 
    password=dbcreds.password,
    host=dbcreds.host, 
    port=dbcreds.port, 
    database=dbcreds.database)

    cursor = conn.cursor()
    return cursor

def cursor_result(cursor, the_procedure, list_of_args=[]):
    cursor.execute(the_procedure, list_of_args)
    result = cursor.fetchall()
    return result



def the_closer(cursor):
    conn=cursor.connection            
    cursor.close()
    conn.close()