data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
                    #6          11                      29                      5           48

def calculate_structure_sum(lst):
    s = 0 #локальная переменная
    for i in lst:
        if isinstance(i, list): #списки
            s += calculate_structure_sum(i)
        elif isinstance(i, dict): #словарь
            s += calculate_structure_sum(list(i.items()))
        elif isinstance(i, int): # числа
            s += i
        elif isinstance(i, str): # строки
            s += len(i)
        elif isinstance(i, set): #множества
            s += calculate_structure_sum(list(i))
        elif isinstance(i, tuple): #кортежи
            s += calculate_structure_sum(list(i))
    return s

result = calculate_structure_sum(data_structure)
print(result)