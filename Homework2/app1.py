# 20P
# 1) Prove that "and" operation takes precedence over "or" operation by setting
# parentheses in the following expression (False or False and True or True)

var = False or False and True or True
print(var)

var1 = False or (False and True) or True
print(var1)

var2 = (False or False) and (True or True)
print(var2)