import math
import module_userdefined
# import module_userdefined as mu
# from module_userdefined import greeting

print(module_userdefined.COLOR)
module_userdefined.display_color()
module_userdefined.greeting('John')

# To get the list of methods and variables available in the builtin / user-defined module,
# the below command can be used.
print(dir(module_userdefined))
print(dir(math))
