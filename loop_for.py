# For loop is used to execute the set of code repeatedly until certain condition met.

# Normal For Loop
for s in 'python':
    print(s)

print("============================================")

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
for d in days:
    print(d)
else:
    print("No more days of a week is left")

print("============================================")

# For Loop with Break
for d in days:
    if d == 'Wed':
        break
    print(d)

print("============================================")

# For Loop with Continue
for d in days:
    if d == 'Thu':
        continue
    print(d)

print("============================================")

# Nested For Loop
for week in ['Week1', 'Week2']:
    for d in days:
        print(week, d)

print("============================================")

# For Loop with no code block
for i in [1, 2, 3, 4, 5]:
    pass
