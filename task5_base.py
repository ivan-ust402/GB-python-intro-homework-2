"""
5) Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
натуральных чисел. У пользователя необходимо запрашивать новый элемент
рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то
новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например,
my_list = [7, 5, 3, 3, 2].
"""
# New comment
def show_rating(array, number):
    """ Showing rating """
    match_in_array = array.count(number)
    if match_in_array > 0:
        index_match = array.index(number)
        array.insert(index_match + match_in_array, number)
    else:
        if number > array[0]:
            array.insert(0, number)
        elif number < array[len(array) - 1]:
            array.append(number)
    return array


my_list = [7, 5, 3, 3, 2]
input_number = int(input("Введите новый элемент рейтинга: "))
print(show_rating(my_list, input_number))
