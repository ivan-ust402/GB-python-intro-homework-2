"""
2) Для списка реализовать обмен значений соседних элементов, т.е. значениями
обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве
элементов последний сохранить на своем месте. Для заполнения списка элементов
необходимо использовать функцию input().
"""
def create_list(array_size):
    """ Creating and Filling list """
    array = []
    i = 0
    for _ in range(array_size):
        array.append(input(f'Введите {i} строчный элемент: '))
    return array


size = int(input("Введите количество элементов списка: "))
my_list = create_list(size)
print(my_list)
