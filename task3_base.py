"""
3) Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому
времени года относится месяц (зима, весна, лето, осень). Напишите решения
через list и через dict.
"""
def find_season_list(number):
    """Show time of year"""
    seasons = ["зима", "весна", "лето", "осень", "нет такого месяца"]
    winter = (12, 1, 2)
    spring = (3, 4, 5)
    summer = (6, 7, 8)
    autumn = (9, 10, 11)
    index = None
    if number in winter:
        index = 0
    elif number in spring:
        index = 1
    elif number in summer:
        index = 2
    elif number in autumn:
        index = 3
    else:
        index = 4
    return seasons[index]

month = int(input("Введите месяц в виде целого числа от 1 до 12: "))
print(find_season_list(month))
