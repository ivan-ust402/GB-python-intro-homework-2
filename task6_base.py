"""
*Реализовать структуру данных «Товары». Она должна представлять собой список
кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно
быть два элемента — номер товара и словарь с параметрами (характеристиками
товара: название, цена, количество, единица измерения). Структуру нужно
сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый
ключ — характеристика товара, например название, а значение — список
значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""
def add_params(params, param_key, param_val):
    """ add parameters in dictionary"""
    params[param_key] = param_val

def add_all_params(index, params):
    """ collect all params in tuple """
    return tuple([index, params])

def get_analytics(products_base_date):
    """Get analytics"""
    analytics_dictionary = {}
    for elem in products_base_date:
        for param_key, param_val in elem[1].items():
            if param_key in analytics_dictionary:
                analytics_dictionary[param_key].append(param_val)
            else:
                analytics_dictionary[param_key] = [param_val]
    return analytics_dictionary

all_products = []
while input('Вы хотите добавить товар? Напишите "да" или "нет": ') == 'да':
    number = int(input("Введите порядковый номер товара: "))
    param_list = {}
    while input('Вы хотите добавить параметр? Напишите "да" или "нет": ') == \
            'да':
        param_name = input('Введите наименование параметра товара: ')
        param_value = input('Введите значение параметра товара: ')
        add_params(param_list, param_name, param_value)
    product = add_all_params(number, param_list)
    all_products.append(product)

print(all_products)
print(get_analytics(all_products))
