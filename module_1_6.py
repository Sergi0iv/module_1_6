my_dict = {'Marina': 1998,'Tolik': 1985,
           'Anna': 1993,'Boris': 1943}
print(my_dict)
print(my_dict.get('Anna'))
print(my_dict.get('Nikolay'))
my_dict.update({'Lena': 1990,'Dima': 1995})
print(my_dict)
del my_dict['Tolik']
print(my_dict)
print(my_dict.get('Tolik'))
print(my_dict)

my_set = {1,4,7,'Anna','Anna',7,7,4}
print(my_set)
my_set.update({5,9,9,5,5,})
print(my_set)
my_set.discard('Anna')
print(my_set)