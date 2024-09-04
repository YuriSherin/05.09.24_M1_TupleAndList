immutable_var = 1, 2, '3', '4', True, [100, 200]
print(immutable_var)

# Кортеж, в отличие от списка, является неизменяемой коллекцией.
# Попытка изменить элемент коллекции приведет к ошибке.
# immutable_var[0] = 10
# print(immutable_var)

# Если кортеж содержит в качестве элемента списки, то элементы такого списка допускают изменения
immutable_var[5][0] = 10
immutable_var[5].append('New String')
print(immutable_var)

mutable_list = [10, 20, '30', 'String', True]
mutable_list[3].upper()
mutable_list[4] = False
mutable_list.append("NewString")
print(mutable_list)
