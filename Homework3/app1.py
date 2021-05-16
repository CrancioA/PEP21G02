# 25P
# Write a function that takes in a list of objects and converts each object in the list into a int.
# For objects that can't be directly converted to int should have their length counted
# The function will return a list with a int values ordered from largest to smallest.
# example [1, True, '123', False, 6, ()] will be transformed into [123, 6, 1, 1, 0, 0]

def ordered_ints(list_of_objects: list):
    converted_list = []
    sorted_list = []
    for i in list_of_objects:
        if type(i) is int:
            converted_list.append(i)
        elif type(i) is str or type(i) is bool or type(i) is float:
            converted_list.append(int(i))
        else:
             converted_list.append(len(i))
        sorted_list = sorted(converted_list, reverse=True)

    return sorted_list


print(ordered_ints([1, True, '123', False, 6, ()]))
