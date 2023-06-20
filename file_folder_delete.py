import os
import shutil

folder_name = input('Enter the folder name \n')
try:
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name)
    else:
        print(folder_name, "does not exists")
except Exception as ex:
    print(ex)
