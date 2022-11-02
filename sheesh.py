
# Дан список [ 5, 3, 8, 13, 5, 6, 8, 15, 13, 5, 5, 8, ]

# Напишите функцию принимающую в себя этот список. Она должна возвращать следующий словарь:

# {3: 6, 5: 10, 6: 12, 8: 16, 13: 26, 15: 30, 'source': [3, 5, 6, 8, 13, 15], 'total': 50}

lst = [5, 3, 8, 13, 5, 6, 8, 15, 13, 5, 5, 8,]

def to_dict(lst):
    dict_el = {element: element*2 for element in lst}
    source = {'source': list(set(lst))}
    sum_source = {'total': sum(source.get('source'))}


    my_dict = {}
    my_dict.update(dict_el)
    my_dict.update(source)
    my_dict.update(sum_source)
    return my_dict

print(to_dict(lst))




# Дается 2 строки "Aidana" и "Adilet" . Вам нужно в результате получить смешанную строку из двух имен, буква за буквой.
# Результат: "AAiddialneat"
# В решении обязательно должнен испрользоваться цикл for

# s = ("Aidana")
# v = ("Adilet")

# s = list(s)
# v = list(v)

# count = 0
# place = 1
# for i in range(len(v)):
#     s.insert(place, v[count])
#     count +=1
#     place +=2
# print(''.join(s))