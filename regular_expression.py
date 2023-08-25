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

