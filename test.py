file = open('test1.txt', 'w', encoding="utf8")

# for i in file.readlines():
#     print(i)

# file.close()

with open('test.txt', 'w', encoding="utf8") as f:
    for i in file.readlines():
        print(i)

# str_gen = [word for word in range(15)]
# str_gen2 = str_gen.copy() [::-1]

# #for i in range(len(str_gen)):
#     file.write(f'{str_gen[i]}     {str_gen2[i]}\n')

