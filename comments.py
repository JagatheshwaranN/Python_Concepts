# In Python, we have only single line comment, and it can be done using the '#' symbol.
# People sometimes got confuse with doc string as multiline comments. But python doesn't have multiline comment.

# The below code snippet print python
print('python')

# Doc string can be represented using single or double triple quotes.
# By default, the doc string is ignored by the interpreter.
# To print the doc string, we have __doc__ function in python.

"""
This is example 
for doc string.
"""
print(__doc__)  # Ideally it should print doc string, but it prints None.

docStr = """
This is example 
for doc string.
"""
print(docStr)
