import copy

# Shallow Copy
# ============
# If the original object contains any references to mutable objects, just duplicate
# reference variables will be created pointing to old contained objects. But not
# duplicate objects creation.
lst1 = [10, 20, [30, 40], 50]
lst2 = copy.copy(lst1)
# lst2 = lst1.copy()
print(id(lst1))
print(id(lst2))
print(id(lst1[2]))
print(id(lst2[2]))
lst1[0] = 100
print(lst1)
print(lst2)
# When we update the nested object [30, 40], then the change will reflect in both L1 and L2.
# Because for nested objects duplicate copy won't be created.
lst1[2][0] = 300
lst1[2][1] = 400
print(lst1)
print(lst2)

# Deep Copy
# =========
# If the original object contains any references to mutable objects, instead of duplicate
# reference variables, the mutable objects copy will be created.
lst1 = [10, 20, [30, 40], 50]
lst2 = copy.deepcopy(lst1)
print(id(lst1))
print(id(lst2))
print(id(lst1[2]))
print(id(lst2[2]))
lst1[0] = 100
print(lst1)
print(lst2)
# When we update the nested object [30, 40], then the change will reflect in both L1 and L2.
# Because for nested objects duplicate copy won’t be created.
lst1[2][0] = 300
lst1[2][1] = 400
print(lst1)
print(lst2)

# Note:
# If original object doesn't contain any nested objects, then we should go for Shallow copy / cloning.
# Note: If original object does contain any nested objects, then we should go for Deep copy / cloning.
