# dict

empty_dict = {}

my_dict = {1: 'one', 'two': 2, 3: [], 4: {}}
print(my_dict)

# hash

print('one'.__hash__())
# print([1,2,3].__hash__())

# dict methods

print(my_dict.keys())
print(type(my_dict.keys()))
for key in my_dict.keys():
    print(key)

print(80*'#')

for value in my_dict.values():
    print(value)

print(80*'#')

for item in my_dict.items():
    print(item)

for key, value in my_dict.items():
    print('key:', key, 'value:', value)

#get value
print(my_dict[1])
print(my_dict.get(1))
# print(my_dict[2])
print(my_dict.get(2, 'Not a value'))

x = [[1,2,3],[3,4,5]]
for i in x:
    print(i)

# calculate factorial

def factorial(number):
    product = 1
    for i in range(1, number+1):
        product = product * i
    return product

var1 = factorial(6)
print(var1)

#recursivitate

def factorial1(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

var1 = factorial(6)
print(var1)

#append vs extend

a = [1, 2, 3]
b = [1, 2, 3]
a.extend(b)
print(a)

# sets

my_empty_set = set()
print(my_empty_set)

my_set = set([1,2,3,3])
print(my_set)

set_a = set([1,2,3,4])
set_b = set([3,4,5,6])

#set operations
result = set_a.union(set_b)
print(result)

result = set_a.difference(set_b)
print(result)

result = set_b.difference(set_a)
print(result)

# result = set_a.difference_update(set_b)
# print(set_a)

result = set_a.symmetric_difference(set_b)
print(result)

result = set_a.symmetric_difference_update(set_b)
print(set_a)

# local, nonlocal, global variables

g_var1 = 'a'

def check_g():
    global g_var1
    g_var1 += 'c'
    ln_var1 = 'd'
    print(g_var1)
    def check_n():
        nonlocal ln_var1
        print('in n function:', ln_var1)
    check_n()

check_g()
print(g_var1)
g_var1 = 'c'
print(g_var1)