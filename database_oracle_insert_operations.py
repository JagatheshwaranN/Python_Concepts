import cx_Oracle

# Insert Record
connection = cx_Oracle.connect(user='JAGA', password='ALLOWME', dsn='localhost/XEPDB1')
try:
    statement = connection.cursor()
    query = ('insert into Person(Name, Age, City) '
             'values(:name,:age,:city)')
    column_values = ('John', 29, 'Texas')
    statement.execute(query, column_values)
    connection.commit()
except Exception as ex:
    print(ex)
finally:
    connection.close()

print("=====================================")

# Insert Multiple Records
connection = cx_Oracle.connect(user='JAGA', password='ALLOWME', dsn='localhost/XEPDB1')
try:
    statement = connection.cursor()
    query = ('insert into Person(Name, Age, City) '
             'values(:name,:age,:city)')
    rows = [('Blake', 27, 'Arizona'), ('Eric', 25, 'Hawaii')]
    statement.executemany(query, rows)
    connection.commit()
except Exception as ex:
    print(ex)
finally:
    connection.close()
