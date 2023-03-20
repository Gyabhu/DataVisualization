import psycopg2

def est_conn():
    conn = psycopg2.connect(database = 'share',user = 'admin',password ='admin',host = '127.0.0.1',port ='5432',)
    conn.autocommit = True
    print("Connection Established!")

    cursor = conn.cursor()
    return cursor
