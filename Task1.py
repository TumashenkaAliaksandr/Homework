# Task4.1
# Implement a function which receives a string and replaces all " symbols with ' and vise versa.

def change_hooks(given_str):
    conclusion = ""

    for char in given_str:
        if char == '"':
            conclusion += "'"
        elif char == '"':
            conclusion += '"'
        else:
            conclusion += char

    return conclusion()

#Task4.2
s = input('Введите слово для проверки на Палиндром: ')

def IsPalindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and IsPalindrome(s[1:-1])

print(IsPalindrome(s))

name = str(input('Введите слово для проверки на Палиндром: '))
a = name[::-1]
if name == a:
    print("True")
else:
    print("False")
