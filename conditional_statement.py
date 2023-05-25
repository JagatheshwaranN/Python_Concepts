# In python, we have if, elif, and else conditional statements.

# if - elif - else flow
stockVal = int(input("Enter the stock value : "))
if stockVal <= 0:
    print("The stock value is less than or equal to Zero")
elif 0 < stockVal <= 100:
    print("The stock value is between 1 and 100")
else:
    print("The stock value is greater than 100")

# nested if flow
x = 200
if x > 100:
    print("The value of x is greater than 100")
    if x > 150:
        print("The value of x is greater than 150")

# single line if statement
y = 100
if y > 50: print("The value of y is greater than 50")

# if with no block of code
if stockVal > 0:
    pass
