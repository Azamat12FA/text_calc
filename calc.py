import sys

from num_tran import *


# Создание текстового ответа
def pr_rt_pt(inp, s):
    i = 0
    while inp > 0:
        if inp % 10 == 0:
            inp //= 10
            i += 1
            continue
        else:
            if (i == 0) and (inp % 100 in number_out):
                s = number_out[inp % 100 * 10 ** i] + ' ' + s
                inp //= 10
                i += 2
            else:
                s = number_out[inp % 10 * 10 ** i] + ' ' + s
                i += 1
            inp //= 10
    return s[:-1]


# Преобразует число в строку
def print_result(res):
    if '.' not in str(res):
        if res == 0:
            return 'ноль'
        else:
            resultat = ''
            while res > 0:
                if res // 1000 != 0:
                    i = 0
                    while res // 1000 != 0:
                        if res // 1000 % 10 == 1:
                            resultat = pr_rt_pt(res % 1000, '') + ' ' + resultat
                            res //= 1000
                            i += 1
                            resultat = number_out[10 ** 3 ** i][:-1] + 'а ' + resultat
                        else:
                            resultat = pr_rt_pt(res % 1000, '') + ' ' + resultat
                            res //= 1000
                            i += 1
                            resultat = number_out[10 ** 3 ** i] + ' ' + resultat
                else:
                    if res // 1000 % 10 == 1:
                        resultat = pr_rt_pt(res % 1000, '') + ' ' + resultat
                        res //= 1000
                    else:
                        resultat = pr_rt_pt(res % 1000, '') + ' ' + resultat
                        res //= 1000
    else:
        while res % 1 != 0:
            x = int(str(res)[str(res).index('.') + 1:])
            if x % 10 == 1:
                resultat = number_out_drob[len(str(res)[str(res).index('.') + 1:])][0]
            else:
                resultat = number_out_drob[len(str(res)[str(res).index('.') + 1:])][1]
            while x > 0:
                if x // 1000 != 0:
                    i = 0
                    while x // 1000 != 0:
                        if x // 1000 % 10 == 1:
                            resultat = pr_rt_pt(x % 1000, '') + resultat
                            x //= 1000
                            i += 1
                            resultat = number_out[10 ** 3 ** i][:-1] + 'а ' + resultat
                        else:
                            resultat = pr_rt_pt(x % 1000, '') + ' ' + resultat
                            x //= 1000
                            i += 1
                            resultat = number_out[10 ** 3 ** i] + ' ' + resultat
                else:
                    if x // 1000 % 10 == 1:
                        resultat = pr_rt_pt(x % 1000, '') + ' ' + resultat
                        x //= 1000
                    else:
                        resultat = pr_rt_pt(x % 1000, '') + ' ' + resultat
                        x //= 1000
            res //= 1
        while res > 0:
            if res // 1000 != 0:
                i = 0
                while res // 1000 != 0:
                    if res // 1000 % 10 == 1:
                        resultat = pr_rt_pt(res % 1000, '') + resultat
                        res //= 1000
                        i += 1
                        resultat = ' ' + number_out[10 ** 3 ** i][:-1] + 'а ' + resultat
                    else:
                        resultat = pr_rt_pt(res % 1000, '') + resultat
                        res //= 1000
                        i += 1
                        resultat = ' ' + number_out[10 ** 3 ** i] + ' ' + resultat
            else:
                resultat = pr_rt_pt(res % 1000, '') + ' и ' + resultat
                res //= 1000
    return resultat


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


# Операция деления и проверка на деление на ноль
def command_split(y, z):
    try:
        x = y / z
        if x % 1 == 0:
            x = int(str(x)[0:str(x).index('.')])
        else:
            x = round(x, 6)
        return x
    except ZeroDivisionError:
        print('На ноль делить нельзя')
        sys.exit()


# Возведение в квадрат
def command_involution(y, z):
    x = y ** z
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
commands = {'степени': command_involution, 'умножить': command_multiplication, 'разделить': command_split,
            'минус': command_minus, 'плюс': command_plus}
x = commands.keys()
for i in st:
    if 'на' == i:
        st.remove('на')
    elif 'в' == i:
        st.remove('в')

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

# Проверка на правильность введёного выражения
if len(st) < 3:
    print('Проверьте правильность введёного выражения')
    sys.exit()
for j in x:
    while j in st:
        index = st.index(j)
        st, index = command_checking_number(st, index)
        result = commands[j](st[index - 1], st[index + 1])
        del st[index - 1:index + 2]
        st.insert(index - 1, result)

print(print_result(result))
