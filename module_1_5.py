immutable_var = [1, 2], 'b', 'a'
print(immutable_var)
print(type(immutable_var))
#immutable_var[0][1] = 2
#print(immutable_var) - кортеж не изменяется

mutable_list = list(immutable_var)
print(mutable_list)
mutable_list[0][0] = 5
print(mutable_list)
print(type(mutable_list))