import psycopg2
hostname = 'sqlserver'
username = 'postgres'
password = 'password'
database = 'postgres'

def doSelect( conn ) :
    cur = conn.cursor()

    cur.execute( "SELECT * FROM EXAMPLE" )

    values = []
    for record in cur.fetchall() :
        values.append(record)

    return values

def doInsert( conn, name, surname) :
    cur = conn.cursor()

    cur.execute("INSERT INTO EXAMPLE (NAME, SURNAME) VALUES (%s, %s)", (name, surname))
    conn.commit()

def getConnection():
    return psycopg2.connect( host=hostname, user=username, password=password, dbname=database)