#while

def add_numbers():
    my_list = []
    total = 0
    while total <= 100:
        if total == 100:
            break
        number = int(input("Enter numbers: "))
        if number >= 0:
            total = total + number
            my_list.append((number))
    else:
        return total
    return my_list

print(add_numbers())
