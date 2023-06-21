import cx_Oracle

# Fetch All Records
connection = cx_Oracle.connect(user='JAGA', password='ALLOWME', dsn='localhost/XEPDB1')
try:
    statement = connection.cursor()
    result_set = statement.execute('Select * from Employee')
    records = result_set.fetchall()
    for record in records:
        print(record)
except Exception as ex:
    print(ex)
finally:
    connection.close()

print("====================================")

# Fetch First Record
connection = cx_Oracle.connect(user='JAGA', password='ALLOWME', dsn='localhost/XEPDB1')
try:
    statement = connection.cursor()
    result_set = statement.execute('Select * from Employee')
    records = result_set.fetchone()
    for record in records:
        print(record)
except Exception as ex:
    print(ex)
finally:
    connection.close()

print("====================================")

# Fetch Many Records
connection = cx_Oracle.connect(user='JAGA', password='ALLOWME', dsn='localhost/XEPDB1')
try:
    statement = connection.cursor()
    result_set = statement.execute('Select * from Employee')
    records = result_set.fetchmany(2)
    for record in records:
        print(record)
except Exception as ex:
    print(ex)
finally:
    connection.close()
