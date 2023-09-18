import cx_Oracle

connection = cx_Oracle.connect(user="JAGA",
                               password="ALLOWME",
                               dsn="localhost/XEPDB1")
if connection is not None:
    print('Connection Established')
    print('Version : ', connection.version)
else:
    print('Connection Not Established')
connection.close()
