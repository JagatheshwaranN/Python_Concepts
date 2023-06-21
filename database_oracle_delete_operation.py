import cx_Oracle

# Delete Record
connection = cx_Oracle.connect(user='JAGA', password='ALLOWME', dsn='localhost/XEPDB1')
try:
    statement = connection.cursor()
    query = 'Delete From Person Where Name=:name'
    delete_value = ('Eric',)
    statement.execute(query, delete_value)
    connection.commit()
except Exception as ex:
    print(ex)
finally:
    connection.close()
