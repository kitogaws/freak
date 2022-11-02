# a = "Aidana"
# b = "Adilet"

# result = ''

# if len(a) != len(b):
#     print('длина должна быть одинаковой')
# else:
#     for i in range(len(a)):
#         result += a[i]+ b[i]


# print(result)

lst = [5, 3, 8, 13, 5, 6, 8, 15, 13, 5, 5, 8,]

def func(arg):
    my_list = sorted(arg)
    my_dict = list(set(my_list))

    for i in range(len(my_dict)):
        my_dict = {number : number + number for number in my_list}

    source = {'source': list(set(my_list))}
    my_dict.update(source)
    total = {'total':sum(list(set(my_list)))}
    my_dict.update(total)

    return my_dict

print(func(lst))