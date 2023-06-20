file_name = input('Enter the file name \n')
file = None
try:
    file = open(file_name, 'a')
    file.write('Python is a superb programming language')
except Exception as ex:
    print(ex)
finally:
    file.close()
    print("File ", file_name, " is closed.")
