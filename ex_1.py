#!/usr/bin/env python3
from librip.gens import field
from librip.gens import gen_random
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]

# Реализация задания 1
#print()
print(field(goods, 'title', 'price'), gen_random(1, 5, 5))

print(list(map(lambda x: x**2, gen_random(1,5,5))))
print([i*i for i in gen_random(1,5,5)])

