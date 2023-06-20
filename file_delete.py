import os

file_name = input('Enter the file name \n')
try:
    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        print(file_name, "does not exists")
except Exception as ex:
    print(ex)