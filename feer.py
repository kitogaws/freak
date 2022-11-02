lst = [1, 2]

while len(lst) <= 31:
    result = lst[-1] + lst[-2]
    lst.append(result)

new_lst = []
result = 0

for i in lst:
    if i % 2 == 0:
        new_lst.append(i)

    if 4000000 <= result < 5000000:
        print(result)
        break


