import oracle_connection
import cx_Oracle

# db = oracle_connection.ConnectOracle('localhost','XEPDB1', 'JAGA', 'ALLOWME')
connection = cx_Oracle.connect(user="JAGA",
                               password="ALLOWME",
                               dsn="localhost/XEPDB1")
print(connection)
statement = connection.cursor()
result_set = statement.execute('Select * from Employee')

for record in result_set:
    print(record)
