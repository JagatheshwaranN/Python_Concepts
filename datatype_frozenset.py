# To represent a group of objects as a single entity we have to go for Collection Data Types.
# When we have requirements to display a group of values as single entity where duplicates not allowed.
# And order is not important, then we can use Set.
# FrozenSet - It is a collection datatype in Python.
# FrozenSet is same as Set with one exception as FrozenSet is immutable.

# Characteristics of FrozenSet
# 1.	Duplicated not allowed.
# 2.	Order is not preserved.
# 3.	Indexing / Slicing not applicable as order is not preserved.
# 4.	Heterogeneous objects allowed.
# 5.	FrozenSet is not growable in nature.
# 6.	FrozenSet is immutable object.
# 7.	FrozenSet can be represented using {}

s = {1, 2, 3, 4, 5, 'a'}
fs = frozenset(s)
print(fs)
print(id(fs))
print(type(fs))

# FrozenSet Add - Not Applicable
# fs.add(6)  # AttributeError: 'frozenset' object has no attribute 'add'

# FrozenSet Remove - Not Applicable
# fs.remove(5)  # AttributeError: 'frozenset' object has no attribute 'remove'

# FrozenSet Copy
fs1 = fs.copy()
print(fs1)