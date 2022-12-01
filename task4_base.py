"""
4) Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""
# New comment
def print_formatting_message(string):
    """ Message Formatting Method """
    intermediate_list = string.split(' ')
    for i, el_list in enumerate(intermediate_list, 1):
        if len(el_list) > 10:
            el_list = el_list[0:10]
        print(f'Строка {i}: {el_list}')

input_string = input("Введите ваше сообщение: ")
print_formatting_message(input_string)
