data_structure = [[1, 2, 3]]

def calculate_structure_sum(lst):
    global  s
    s = 0
    for i in lst:
        if type(i) == list: #списки
            calculate_structure_sum(i)
        elif type(i) == int: # числа
            s += i
        elif type(i) == str: # строки
            s += len(i)
    return print(s)


result = calculate_structure_sum(data_structure)
print(result)