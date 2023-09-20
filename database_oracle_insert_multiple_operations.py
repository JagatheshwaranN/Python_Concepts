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
except cx_Oracle.DatabaseError as ex:
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
except cx_Oracle.DatabaseError as ex:
    print(ex)
finally:
    connection.close()

print("=====================================")

# Insert Multiple Records
connection = cx_Oracle.connect(user='JAGA', password='ALLOWME', dsn='localhost/XEPDB1')
try:
    statement = connection.cursor()
    while True:
        name = input('Enter the person name')
        age = int(input('Enter the person age'))
        city = input('Enter the person city')
        query = "insert into Person values('%s', %d, '%s')"
        statement.execute(query % (name, age, city))
        connection.commit()
        print('Records inserted successfully')
        option = input('Do you want to insert one more record [Yes|No]')
        if option == 'No':
            break
except cx_Oracle.DatabaseError as ex:
    print(ex)
finally:
    connection.close()
