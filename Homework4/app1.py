""" Homework 4  - needs to be presented before exam day"""


# We want to check which of the following function has the smallest minimum for x in range -10, 10 and use that function
# to calculate for x = 0
# 1x^2 -2x + 2
# 2x^2 -4x + 4
# 3x^2 -6x + 6

# 20P
# Create a function (build) that takes 3 int arguments (a, b, c) and return a function (response) that takes one int
# argument (x) and calculates ax^2+bx+c

def build(a, b, c):
    def response(x):
        equation = a * (x ** 2) + b * x + c
        return equation
    return response(0)

# 20P
# Create a list of response functions by calling build function with the arguments (1,-2,2), (2,-4,4), (3,-6,5)
list_of_functions = []
for a, b, c in ((1, -2, 2), (2, -4, 4), (3, -6, 6)):
    list_of_functions.append(build(a, b, c))
print(list_of_functions)

# 20P
# Create a dictionary that contains the result functions as keys and as values the list of results from calling that
# function with x in range -10, 10 as value
dict_of_results = {}
for function in list_of_functions:
    dict_of_results[function] = list_of_functions
print(dict_of_results)

# 20P
# Check dict_of_results and determine which function has the smallest value in the list of values
function_with_smallest_result = None
smallest_value = None
for function, values in dict_of_results.items():
    if smallest_value is None or smallest_value > values:
        smallest_value = values
        function_with_smallest_result = function
print(smallest_value, function_with_smallest_result)

# 20P
# Call function_with_smallest_result with argument x = 0 and print the returned value (you should get 2)
var = function_with_smallest_result
print(var)