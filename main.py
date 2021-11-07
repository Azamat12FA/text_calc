import sys

from num_tran import *


# Преобразует число в строку
def print_result(res):
    if res == 0:
        resultat = 'ноль '
    else:
        resultat = ''
        i = 0
        while res > 0:
            if i == 0:
                x = res % 100
                if (x > 9) and (x < 21):
                    resultat = number_out[x] + ' ' + resultat
                    i = i + 1
                    res //= 10
                elif res % 10 == 0:
                    res //= 10
                    i += 1
                    continue
                else:
                    resultat = number_out[(res % 10) * (10 ** i)] + ' ' + resultat
            else:
                resultat = number_out[(res % 10) * (10 ** i)] + ' ' + resultat
            res //= 10
            i += 1
    return resultat[:-1]


# Операция сложения
def command_plus(y, z):
    x = y + z
    return x


# Операция вычитания
def command_minus(y, z):
    x = y - z
    return x


# Операция умножение
def command_multiplication(y, z):
    x = y * z
    return x


# Проверка чисел на двухзначность
def command_checking_number(sp, inx):
    if inx - 2 >= 0:
        # Проверка первого числа на двухзначность
        if sp[inx - 2] not in commands:
            sp.insert(inx - 1, command_plus(sp[inx - 2], sp[inx - 1]))
            del sp[inx - 2]
            del sp[inx - 1]
            inx -= 1
    if len(sp) - 1 >= inx + 2:
        # Проверка второго числа на двухзначность
        if sp[inx + 2] not in commands:
            sp.insert(inx + 1, command_plus(sp[inx + 2], sp[inx + 1]))
            del sp[inx + 2]
            del sp[inx + 2]
    return sp, inx


s = input('Введите пожалуйста выражение:\n')
# Удаление из строки всех пробелов
st = s.split(' ')


# Создание списка с командами, с учетом приоритета
commands = {'умножить': command_multiplication, 'минус': command_minus, 'плюс': command_plus}
x = commands.keys()
for i in st:
    if 'на' == i:
        st.remove('на')

# Преобразование каждого текстого представления числа, в числовой вид
for i in st:
    if i in commands:
        continue
    else:
        try:
            ind = st.index(i)
            st[ind] = number_in[i]
        except KeyError:
            print('Проверьте правильность выражения!')
            sys.exit()

for j in x:
    while j in st:
        index = st.index(j)
        st, index = command_checking_number(st, index)
        result = commands[j](st[index - 1], st[index + 1])
        del st[index - 1:index + 2]
        st.insert(index - 1, result)

print(print_result(result))
