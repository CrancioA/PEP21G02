multi_dimensional_list = [[1, [2, [3, 15]]], [4, [5, [6, 16]]], [7, [8, [9]]],[[[0]]]]

# result = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def function1(data1:list):
    fin_list = []
    for i in data1:
        if type(i) == int:
            fin_list.append(i)
            continue
    return fin_list


def flatten_list(data:list):
    fin_list = function1(data)
    return fin_list

result = flatten_list(multi_dimensional_list)
print(result)
