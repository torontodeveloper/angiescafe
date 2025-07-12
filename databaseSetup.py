import mysql.connector


sqlDBQuery = 'CREATE DATABASE angiecafe'
orderQuery = 'CREATE TABLE item(id int,item VARCHAR(20),numberItems int)'
insertQuery = 'INSERT INTO item(id,item,numberItems) values(%d,%s,%d)'
values = [(1001,'Cappucino',2),(2001,'Donut',3)]
readOrderQuery = 'SELECT * FROM item'

def db_setup():
    
    try:
        conn = mysql.connector.connect(user='root',password='root')

        cursor = conn.cursor()
        cursor.execute('SHOW DATABASES')
        for db in cursor:
            print('DB',db)
        cursor.execute(sqlDBQuery,values)
        print('Database connection executd SUCCESSFUlly')
    except Exception as ex:
        print('Database Exception',ex)
        conn.close()

def query_execution(query):
    id = 1001
    item ='Dosa'
    numberItems=2
    sql = f"INSERT INTO item(id, item,numberItems) VALUES ({id},{item},{numberItems})"
    try:
        conn = mysql.connector.connect(user='root',password='root',database='angiecafe')

        cursor = conn.cursor()
        cursor.execute(sql)
        print('QUERY executed succefuylly')
    except Exception as ex:
        print('Database Exception',ex)

def read_orders(query):
    print('read orders',query)
    try:
        conn = mysql.connector.connect(user='root',password='root',database='angiecafe')
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(f'row is {row}')
        return rows
        
    except Exception as ex:
        print('Database Exception',ex)
        conn.close()

def run():
    db_setup()
    # query_execution(sqlDBQuery)
    # query_execution(orderQuery)
    # query_execution(insertQuery)
    read_orders(readOrderQuery)
if __name__=='__main__':
   run()
