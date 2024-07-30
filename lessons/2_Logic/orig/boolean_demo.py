"""
Boolean Variable Demo
"""

# Boolean is a variable type that has two values:
#   True
#   False
# Just like int, double, and string variables, boolean variables can be
# created by writing the variable name followed by = True or = False
#   boolean_var = True
#   boolean_var = False
#
# Boolean variables or values can be used directly in if and elif statements:
#   boolean_var = True
#   if boolean_var:
#       print('boolean_var was True!')
#
# Notice that if boolean_var == True: isn't necessary.
#
# Boolean values are created when doing inequality comparisons (<, > ==)
# between variables or values
#   boolean_var = 5 == 5            # True
#   is_Keith = name == 'Keith'      # True
#   is_weekday = day == 'Saturday'  # False
#
# Boolean variables can be toggled, i.e. switched, using the 'not' keyword
#   boolean_var = True
#   boolean_var2 = not boolean_var  # False

# Two boolean variables
boolean_var1 = True
boolean_var2 = False

# NOTE - boolean_var1 == True is not necessary
if boolean_var1:
    print('boolean_var1 is True!')
    if boolean_var2:
        print('boolean_var2 is True!')
    else:
        print('boolean_var2 is False!')
else:
    print('boolean_var1 is False!')

boolean_var3 = True
for i in range(4):
    print('boolean_var3 is: ' + str(boolean_var3))
    boolean_var3 = not boolean_var3
