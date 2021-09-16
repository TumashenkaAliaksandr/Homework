# Task 1.6
# Write a program which makes a pretty print of a part of the multiplication table. Examples:
#
# Input:
# a = 2
# b = 4
# c = 3
# d = 7
#
# Output:
# 	3	4	5	6	7
# 2	6	8	10	12	14
# 3	9	12	15	18	21
# 4	12	16	20	24	28

a = 2
b = 4
c = 3
d = 7
count = 0
print(' ', end ='\t')
for j in range(c,d+1) :
    print(j, end ='\t')
print()
for i in range(a,b+1) :
    for j in range(c,d+1) :
        if count < 1:
            print(i, end ='\t')
            count += 1

        print(i*j, end ='\t')
    print()
    count = 0



print(end='\n')
print('-------------------------------------')

# Task 1.6
# Write a Python program to convert a given tuple of positive integers into an integer. Examples:
#
# Input: (1, 2, 3, 4)
# Output: 1234
given_tuple = (1, 2, 3, 4, 5)
print("Input : " + str(given_tuple))
res = int(''.join(map(str, given_tuple)))
print("Output : " + str(res))

#Task1.1
#Длинна строки без функции len
def alexWin(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter

str = "EPAM+Pegasus=👍"
print(alexWin(str))

print(end='\n')
print('-------------------------------------')
#Task 1.2
s = 'Oh, it is python'.lower() # lower учитывает нижний и верхний регистр
my_dict = {i: s.count(i) for i in s}  # функция count(), считает количество вхождений элемента в строку
print(my_dict)
#второй способ
# s ='Oh, it is python'.lower()
# unique = dict(zip(list(s), [list(s).count(i) for i in list(s)]))
# print(unique)

print(end='\n')
print('-------------------------------------')
#Task1.3
#l = ['red', 'white', 'black', 'red', 'green', 'black']
#Output: ['black', 'green', 'red', 'white', 'red']

s = ['red', 'white', 'black', 'red', 'green', 'black']
l = s[:-5]
l1 = sorted(set(s[:-1]))
l2 = l1+l
print(l2)

print(end='\n')
print('-------------------------------------')
#Task1.3(1)
#Input: 60
#Output: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}

s = int(input('Please enter a number:'))
c = [x for x in range (1, s // 2 + 1) if s % x == 0] + [s]
print (c)

s = int(input('Please enter a number:'))
for d in range (1, s // 2 + 1) :
  if s % d == 0 :
    print (d, ' ', sep = '', end = '')
print (s)


print(end='\n')
print('-------------------------------------')

#Task1.4
b={8:'family', 7:'huge', 6:'a', 5:'have', 4:'I', 3:'that', 2:'learned', 1:'I'}
a=list(b.keys())
a.sort()
for i in a:
    print(i, b[i])

books = {
("Эдгар Берроуз", "Рэй Брэдбери", 100),
("Трудно быть богом", "Братья Стругацкие", 250),
("Я Робот", "Айзек Азимов", 300),
("Голос тех, кого нет", "Орсон Скотт Кард", 170)
}
print( sorted(books, key=lambda x: x[2]) )

d ={2: 'learned', 1: 'I', 3: 'that', 5: 'have', 4: 'I', 6: 'a', 8:'family', 7:'huge'} #I learned that I have a huge family
print(sorted(d.items()))
print(sorted(d.keys()))
a = dict(sorted(d.items(), key=lambda x: x[0]))
print("After sorting by key: ", a)


print(end='\n')
print('-------------------------------------')

#Task1.5
# Write a Python program to print all unique values of all dictionaries in a list. Examples:
#
# Input: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
l = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print("Input: ",l)
s_val = set( val for dic in l for val in dic.values())
print("Output: ", s_val) #print("Output: ",sorted(s_val))

print(end='\n')
print('-------------------------------------')