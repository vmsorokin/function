def print_params(a = 1, b = 'Строка', c = True):
    print(a, b, c)

print_params()
print_params(4,'Str')
print_params(4, 5, 7)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = ['Yes', 6, False]
values_dict = {'a': 14, 'b':False, 'c':"No"}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['Good', 15]
print_params(*values_list_2, 42)
print_params(4, *values_list_2)