import re

# Regular Expression
# If we want to represent the group of strings according to a particular pattern.
# Then we should go for Regular Expression.

# Main Important Application Areas
# 1.	Validations.
# 2.	To develop Pattern Matching applications (Ctrl F in Windows and Grep in Unix).
# 3.	Translators like Compilers, Interpreters and Assemblers.
#       Compiler Design - Lexical Analysis (Scanning), Syntax Analysis (Parsing) and Semantic Analysis.
# 4.	To develop digital circuits.
# 5.	To develop communication protocols TCP/IP.

# To work with regular expression in Python, we have to use the RE module.
# RE module functions
# 1.	Compile() function
# 2.	Finditer() function
#       1.	start() – Start index of the match
#       2.	end() – End+1 index of the match
#       3.	group() – Returns the matched String

pattern = re.compile('python')
print(type(pattern))

matcher = pattern.finditer('Learning python is easy')
print(matcher)

count = 0
pattern = re.compile('because')
matcher = pattern.finditer('No sentence can end with because because, because is a conjunction.')
# matcher = re.finditer('because', 'No sentence can end with because because, because is a conjunction.')
for match in matcher:
    count += 1
    print('Match is available at with starting index : ', match.start())
    print('Start:{}, End:{}, Group:{}'.format(match.start(), match.end(), match.group()))
print('Number of occurrences of Match is : ', count)

# match
# We can use this function to check the given pattern at beginning of the target string.
# If match found, then return the match object otherwise none.
data = input('Enter the string to check the pattern \n')
matcher = re.match(data, 'because')
if matcher is not None:
    print('Match is available at the beginning')
    print('Start:{}, End:{}'.format(matcher.start(), matcher.end()))
else:
    print('Match is available at the beginning')

# full match
# We can use this function to check the given pattern fully matches the target string.
# If full match found, then return the match object otherwise none.
data = input('Enter the string to check the pattern \n')
matcher = re.fullmatch(data, 'because')
if matcher is not None:
    print('Full String Match is available')
    print('Start:{}, End:{}'.format(matcher.start(), matcher.end()))
else:
    print('Full String Match is available')

# search
# We can use this function to check the given pattern match the first occurrence.
# If full match found, then return the search object otherwise none.
data = input('Enter the string to check the pattern \n')
matcher = re.search(data, 'No sentence starts with because because because is conjunction')
if matcher is not None:
    print('Match is available')
    print('First occurrence with Start:{} and End:{}'.format(matcher.start(), matcher.end()))
else:
    print('Match is not available')

# findAll
# We can use this function to find all the pattern match.
lst = re.findall('[0-9]', 'a7b9k6z')
print(lst)
