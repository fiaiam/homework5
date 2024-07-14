immutable_var = (1, [5,6,7], 'Hello')
print(immutable_var)
#Изменить сможем только элементы списка внутри кортежа, поскольку элементы самого кортежа неизменяемы
#Изменим значение элемента внутри списка, например, второй (число 6):
immutable_var [1][1] = 9
print('Immutable tuple: ', immutable_var)
#3
mutable_list = [2020, 'im in the list', [999, 1000, 1001]]
print(mutable_list)
mutable_list [0] = 2121
mutable_list [1] = 'im in the list again'
mutable_list [2][2] = 2024
print('Mutable list: ', mutable_list)