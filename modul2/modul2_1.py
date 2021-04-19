# name = 'john'
# age = 26
#
# print('name: ', name, ' age: ', age)
#
# result = type(name)
# print(result)
# result = type(age)
# print(result)
#
# print(5*name)
# result1 = 5*name
# result2 = type(result1)
# print(result2)
#
#
# result = id(name)
# print(result)

# print(8 + 8)
# print((8).__add__(8))
#
# print(8 * 'text ')
# print((8).__mul__(' text'))
# print(('text ').__mul__(8))

# print(8-8)
# print((8).__sub__(8))
#
# print(8/8)
# print((8).__truediv__(8))
#
# Float
#
# result = 8 / 8
# result1 = type(result)
# print(result1)

# print(8**8)
# print((8).__pow__(8))
# print(pow(8, 8))

a = 3
b = 4
c = 5

# x = (-b + ((b**2) - 4 * a * c)**(1/2))/(2*a)
# print(x)
#
# x = (-b - ((b**2) - 4 * a * c)**(1/2))/(2*a)
# print(x)

#prin metode
bsqr = b.__pow__(2)
mul = (4).__mul__(a.__mul__(c))
dif1 = bsqr.__sub__(mul)
print(type(dif1))
var = (1).__truediv__(2)
dif1 = float(dif1)
rad = dif1.__pow__(var)
print(type(var))
print(type(rad))
b = complex(b)
dif2 = (-b).__sub__(rad)
print(type(dif2))
mul1 = (2).__mul__(a)
impartire = dif2.__truediv__(mul1)
x = impartire
print(x)

#Complex

nr1 = 1.0 + 1.0j
nr2 = 3 + 5j
print(nr1+nr2)
#print(type(nr))

#Strings
my_str1 = 'my string \n no multi string'
print(my_str1)
my_str1 = '''this is
a multi string
'''
print(my_str1)

my_str2 = r"my string2 \n no multi line"
print(my_str2)
my_str2 = """my string2 {my_str1}"""
print(my_str2)

#dir
info = dir(my_str2)
print(info)

var1 = 'this is {}'
cap = var1.capitalize()
print(cap)
format1 = var1.format('Sparta')
print(format1)

phone = '0747.655.444'
split1 = phone.split("7")
print(split1)
split1 = phone.rsplit(sep='.', maxsplit=1)
print(split1)
split1 = phone.split(sep='.', maxsplit=1)
print(split1)

#input
# print(input('give me your name: '), var1)

#slice
text = "My text"
first_letter = "My text"[0]
print(first_letter)
slice1 = text[1:4]
print(slice1)
slice2 = text[0:7:1]
print(slice2)

#exercitiu
#text = input('Enter text here: ')
slice1 = text[0:5]
slice2 = text[5:10]
print(slice2 + slice1)

#negative slice/step
reverse = text[::-1]
print(reverse)

reverse1 = slice1[::-1]
reverse2 = slice2[::-1]
print(reverse2 + reverse1)

#true, false
my_bool = True
print(type(my_bool))

print(id(False))
print(id(True))
print(id(10))

print(True + False)
print(dir(True))
x = True.__add__(False)
print(x)

#None
my_none = None
print(type(None))
x = print('')
print(x)
print(dir(my_none))

print(bool(0+0j))
print(bool(0.0))
