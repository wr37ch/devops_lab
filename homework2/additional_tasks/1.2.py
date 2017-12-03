# Есть два списка разной длины. В первом содержатся ключи, а во втором значения.
# Напишите функцию, которая создаёт из этих ключей и значений словарь. Если ключу не
# хватило значения, в словаре должно быть значение None. Значения, которым не хватило
# ключей, нужно игнорировать.

import random
values = random.sample(range(1, 100), 50)
keys = ['apple', 'orange', 'pineapple', 'pear', 'strawberry', 'banana']
def lists_to_dict(keys, values):
    if len(keys) > len(values):
        for x in range(len(keys) - len(values)):
            values.append(None)
    dictionary = dict(zip(keys, values))
    print(dictionary)


lists_to_dict(keys, values)
