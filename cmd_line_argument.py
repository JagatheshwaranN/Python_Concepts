from sys import argv

# argv is a commandline argument used to take the input from command line. It treats the value
# as Str type. It is used to separate the values using the space. If the input is having space
# then compulsory we should enclose the value inside the double quotes.

print("The number of cmdline arguments ", len(argv))
print("The list of cmdline arguments ", argv)
print("The cmdline arguments one by one")
for arg in argv:
    print(arg)
