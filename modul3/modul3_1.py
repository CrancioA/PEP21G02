# functions

# general construction

def my_function(arg1, arg2, arg3, kwarg1=' ', kwarg='\n'):
    print(arg1, arg2, arg3, sep=kwarg1, end=kwarg)
    return arg1 + arg2 + arg3


my_var1 = my_function('srt1', 'str2', 'str3', '#', '$')
print('\n' + 80 * '#')
print(my_var1)


# create function for determining prime number

def is_prime(number):
    for i in range(2,number):
        if (number % i) == 0:
            return False
    return True


print(is_prime(3))
print(is_prime(25))

#list

# empty_list = []
# my_list1 = [1,2,3]
# print(my_list1)
# my_list1.append(4)
# print(my_list1)
#
# empty_list.append(10)
# print(empty_list)

# def primes(limit):
#     result = []
#     for i in range(1,limit + 1):
#         if is_prime(i) is True:  #sau if is_prime(i)
#             limit.append(i)
#     return result

# print(primes(10))

#bit operation

# 01010001
# 01110011

# 01110011 - OR
# 01010001 - AND
# 00100010 - XOR
################

# 00100010
# 01110011

# 01010001

# numbers in memory

0 # 00000000000000...000
1 # 00000000000000...001
2 # 00000000000000...010

# And
print(10 & 11)
print((10).__and__(11))

10 # 0000000000000...1010
11 # 0000000000000...1011
# 0000000000000000...1010

# OR
print(10 | 11)
print((10).__or__(11))
10 # 0000000000000...1010
11 # 0000000000000...1011
# 0000000000000000...1011

# XOR
print(10 ^ 11)
print((10).__xor__(11))
10 # 0000000000000...1010
11 # 0000000000000...1011
# 0000000000000000...0001

# XOR negative number
print(-1 ^ 3)
print((-1).__xor__(3))
-1 # 1111111111111...1111
3  # 0000000000000...1011
#    1111111111111...1100

