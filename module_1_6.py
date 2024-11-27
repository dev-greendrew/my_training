#Словарь
my_dict = {'Andrey': 2005, 'Gleb': 2002, 'Murad': 2004}
print(my_dict)
print(my_dict['Andrey'])
my_dict['Egor'] = 1999
print(my_dict['Egor'])
my_dict.update({'Misha': 1998,
                'Vladimir': 1993})
print(my_dict)
my_dict.pop('Egor')
print(my_dict)

#Множества
my_set = {'String', 1, 2.3, 1, 2, 1, 2, 3, 2}
print(my_set)
list_ = [1, 1, 2, 3, 4, 4, 2, 3, 4, 5, 6, 7, 8, 9]
list_ = set(list_)
print(list_)
print(list_.remove(1))
print(list_)
print(list_.add(12))
print(list_)
