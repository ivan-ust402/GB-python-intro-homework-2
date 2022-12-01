"""
2) Для списка реализовать обмен значений соседних элементов, т.е. значениями
обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве
элементов последний сохранить на своем месте. Для заполнения списка элементов
необходимо использовать функцию input().
"""
# New comment
def create_list(array_size):
    """ Creating and Filling list """
    array = []
    for i in range(array_size):
        array.append(input(f'Введите {i} строчный элемент: '))
    return array

def replace_pair(array):
    """ Replace pair elements of list"""
    i = 0
    result = array.copy()
    if len(result) % 2 == 0:
        while i < len(array):
            if i % 2 == 0 or i == 0:
                temp = result[i]
                result[i] = result[i + 1]
                result[i + 1] = temp
            i += 1
    elif len(result) % 2 != 0:
        while i < len(result)-1:
            if i % 2 == 0 or i == 0:
                temp = result[i]
                result[i] = result[i + 1]
                result[i + 1] = temp
            i += 1
    return result

def replace_pair_another(array):
    """ Replace pair elements of list"""
    size_of_array = len(array)
    if size_of_array % 2 == 0:
        for i in range(0, size_of_array):
            if i % 2 == 0 or i == 0:
                array[i], array[i + 1] = array[i + 1], array[i]
    elif size_of_array % 2 != 0:
        for i in range(0, size_of_array - 1):
            if i % 2 == 0 or i == 0:
                array[i], array[i + 1] = array[i + 1], array[i]
    return array

size = int(input("Введите количество элементов списка: "))
my_list = create_list(size)
print(my_list)
result_list = replace_pair(my_list)
print(result_list)
result_list_another = replace_pair_another(my_list)
print(result_list_another)
