import cx_Oracle

# Fetch All Records
connection = cx_Oracle.connect(user='JAGA', password='ALLOWME', dsn='localhost/XEPDB1')
try:
    statement = connection.cursor()
    result_set = statement.execute('Select * from Employee')
    records = result_set.fetchall()
    file = open('select_results.txt', 'w')
    for record in records:
        print(record)
        file.write(str(record)+'\n')
except cx_Oracle.DatabaseError as ex:
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
except cx_Oracle.DatabaseError as ex:
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
except cx_Oracle.DatabaseError as ex:
    if connection:
        connection.rollback()
        print(ex)
finally:
    if connection:
        connection.close()