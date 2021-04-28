# create function for determining prime number

def is_prime(number):
    for i in range(2,number):
        if (number % i) == 0:
            return False
    return True


print(is_prime(3))
print(is_prime(25))

#list

empty_list = []
my_list1 = [1,2,3]
print(my_list1)
my_list1.append(4)
print(my_list1)

empty_list.append(10)
print(empty_list)

def primes(limit):
    result = []
    for i in range(1,limit + 1):
        if is_prime(i) is True:  #sau if is_prime(i)
            limit.append(i)
    return result

print(primes(10))