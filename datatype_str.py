# Any sequence of chars within single or double quotes is treated as String in Python.
# In Python, we don’t have any char data type. Even single char inside single quote is treated as String in Python.
# Triple quotes can be used to define the Doc String.

a = 'python'
print(a)
print(type(a))
print(id(a))

b = "program"
print(b)
print(type(b))
print(id(b))

# We can even use triple quotes in Python. It is used to represent the multiline string literals.
# We can use single quote 3 times or double quotes 3 times for triple quote.
c = ''' Python
        Course Learning'''
print(c)
print(type(c))
print(id(c))

# If we want to use single quote as a normal character in a string then it should be enclosed within double quotes.
# The vice versa is applicable.
d = "I like 'clever' persons"
print(d)
e = 'I like "clever" persons'
print(e)
f = """I like "clever" persons who is 'honest' in all actions"""
print(f)

# Index can be used to identify the char value from the sequence of chars as String.
# Python provides support for both positive and negative index.
# Positive index goes in forward direction whereas negative index goes in backward direction.
g = 'python'
print(g[0])
print(g[-1])

# Slice operator is used to get the sub string of the given string in Python.
# Syntax is S[begin:end]
# Slice returns substring(slice) from begin index to end-1 index.
# If the begin index is not specified it will consider 0th index as begin index.
# If the end index is not specified it will consider end of the string as end index.
h = 'abcde'
print(h[1:3])
print(h[:3])
print((h[1:]))
print(h[:])
print(h[1:10])  # It will consider only the available values in the given range of index
print(h[3:1])  # Returns empty string
print(h[-1:-3])

# + Operator
# + Operator applicable for the String and if we want to apply the + operator then both variables must be strings.
i = 'python'
print(i[0].upper() + i[1:])
j = 'abcde'
print(j[0].upper() + j[1:len(j) - 1] + j[-1].upper())

# * Operator
# * operator is allowed in Python,and it is called as repetition operator.
# It must take one variable as String and another variable as int.
k = 'python' * 3
print(k)

# String Iterate using For loop
s1 = 'python'

for v in s1:
    print(v)

# String length
print(len(s1))

# String presence check in sentence
s2 = """I like "clever" persons who is 'honest' in all actions"""
print('persons' in s2)

# String UpperCase
s3 = 'python'.upper()
print(s3)

# String LowerCase
s4 = 'PYTHON'.lower()
print(s4)

# String Strip
s5 = ' Hello world '
print(s5.strip())

# String Replace
s6 = 'Happy growing'
print(s6.replace('growing', 'learning'))

# String Split
s7 = 'Hello, World'
print(s7.split(","))

# String format
s8 = 'John'
text1 = 'Hi {}, welcome!'
text1 = text1.format(s8)
print(text1)

s9 = int('200000')
text2 = 'Hi {}, your salary is {:.2f}'
text2 = text2.format(s8, s9)
print(text2)

text3 = 'Hi {0}, your salary is {1}'
text3 = text3.format(s8, s9)
print(text3)

text4 = 'Hi {0}, my brother name is also {0}'
text4 = text4.format(s8)
print(text4)

text5 = 'Hi {name}, your salary is {salary}'
text5 = text5.format(salary=s9, name=s8)
print(text5)

text6 = 'Python'+'Program'
print(text6)

text7 = 'Python','Program'
print(text7)

print('Python','Program')