#take two values from input and divite them
def divide_values():
    my_divide = None
    try:
        x1 = int(input("Enter first number:"))
        x2 = int(input("Enter second number:"))
    except ValueError:
        print("You should enter a number 1-9")
        return None
    try:
        my_divide = x1 / x2
    except TypeError:
        print("x1 & x2 should be integers")
    except ZeroDivisionError:
        print('You should not divide by zero')

    return print(my_divide)

divide_values()



