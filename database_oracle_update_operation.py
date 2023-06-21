import cx_Oracle

# Update Record
connection = cx_Oracle.connect(user='JAGA', password='ALLOWME', dsn='localhost/XEPDB1')
try:
    statement = connection.cursor()
    query = 'Update Person Set Age=:age Where Name=:name'
    update_values = (26, 'Eric')
    statement.execute(query, update_values)
    connection.commit()
except Exception as ex:
    print(ex)
finally:
    connection.close()
