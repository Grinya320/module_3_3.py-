def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
values_list = (False, 578, "Кашак")
values_dict = {'a': False, 'b': 9.24, 'c': "гора"}
print_params(*values_list)
print_params(**values_dict)
values_list2 = ('Лето', 94.58)
print_params(*values_list2, 65)