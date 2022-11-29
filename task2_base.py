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

def replace_pair(array):
    """ Replace pair elements of list"""
    i = 0
    if len(array) % 2 == 0:
        while i < len(array):
            if i % 2 == 0 or i == 0:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
            i += 1
    elif len(array) % 2 != 0:
        while i < len(array)-1:
            if i % 2 == 0 or i == 0:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp
            i += 1
    return array

size = int(input("Введите количество элементов списка: "))
my_list = create_list(size)
print(my_list)
result_list = replace_pair(my_list)
print(result_list)
