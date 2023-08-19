import logging

# Logging is used to log the message to the file. Default logging level is Warning.
# Logging levels as below,
# 1.	Critical = 50
# 2.	Error = 40
# 3.	Warning = 30
# 4.	Info = 20
# 5.	Debug = 10
# 6.	Notset = 0
# By default, the Critical, Error and Warning logging levels will be available to the Programmer.
# Based on requirement, we can set the Info, Debug levels.

logging.basicConfig(filename='log.txt', level=logging.WARNING)
print("Python logging demo")
logging.debug("Debug Message")
logging.info("Info Message")
logging.warning("Warning Message")
logging.error("Error Message")
logging.critical("Critical Message")

# Example
logging.basicConfig(filename='log.txt', level=logging.WARNING)
print("Python logging demo - A new request came")
logging.info('A new request came')
try:
    x = int(input("Enter first number:"))
    y = int(input("Enter second number:"))
    print(x/y)
except ZeroDivisionError as message:
    print("Can't divide number by zero")
    logging.exception(message)
except ValueError as message:
    print("Input should be of type int only")
    logging.exception(message)
logging.info("Request processing completed")


