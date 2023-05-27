# While loop is used to execute the set of code repeatedly until certain condition met.

# Normal While Loop
i = 1
while i <= 5:
    print(i)
    i = i+1

print("=================================")

# While Loop with Break
j = 1
while j <= 5:
    print(j)
    if j == 3:
        break
    j += 1

print("=================================")

# While Loop with Continue
k = 0
while k <= 5:
    k += 1
    if k == 3:
        continue
    print(k)
