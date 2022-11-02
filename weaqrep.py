# s = ['Warner', 'brothers', 'pictures']

# print(s[1][:3])
# print(s[-1][::-1])



# word1 = 'шалаш'
# word2 = 'А роза упала на лапу Азора'
# word2=word2.replace(' ','').lower()
# if word2 == word2 [::-1]:   
#     print ('это слово полидромное')
# else:
#     print('это слово не полидромное')

# print(word2)



# d = '72 101 108 108 111'

# b = d.split(' ')
# for i in b:
#     print(chr(int(i)))
try:
    count = 0
    while count !=3:
        username = input('username: ')
        if '@' not in username and '/' not in username:
            pass1 = input('Password:')
            pass2 = input('Password2:')
            if pass1 == pass2:
                print('Success')
                break
            else :
                print('password not the same')
                count+=1
        else:
            print('your username is not correct')
            count+=1
except NameError:
    print('your name is not correct !!!')