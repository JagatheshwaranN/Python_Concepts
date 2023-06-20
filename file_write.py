file_name = input('Enter the file name \n')
file = None
try:
    file = open(file_name, 'w')
    file.write('Learning Python')
    file.write('\n')
except Exception as ex:
    print(ex)
finally:
    file.close()
    print("File ", file_name, " is closed.")
