immutable_var = True, 17, 22, "Степан", 73.0, [1, 2, 3]
print(immutable_var)
# immutable_var[1] = 10    # Выдается ошибка "кортеж не поддерживает обращение по элементам"
mutable_list = [11, False, "String", 21.7]
mutable_list[1] = True
mutable_list[3] = 12.7
print(mutable_list)