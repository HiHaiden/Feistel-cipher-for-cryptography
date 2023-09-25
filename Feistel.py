# Программа Python для демонстрации
# Алгоритм шифрования Фейстеля

import binascii


# Генерация случайных битов ключа
def rand_key(p):
    import random
    key1 = ""
    p = int(p)

    for i in range(p):
        temp = random.randint(0, 1)
        temp = str(temp)
        key1 = key1 + temp

    return (key1)


# Функция для реализации битового удаления
def exor(a, b):
    temp = ""

    for i in range(n):

        if (a[i] == b[i]):
            temp += "0"

        else:
            temp += "1"

    return temp


# Определение функции BinarytoDecimal()
def BinaryToDecimal(binary):
    # Использование функции int для преобразования в
    # строку
    string = int(binary, 2)

    return string


# Шифр Фейстеля
PT = "Tsapenko Danil KMD-19 DONNTU"

# Деление текста на блоки
# Bloki = PT.split(',')
# Bloki0 = Bloki[0]
# Bloki1 = Bloki[1]
# Bloki2 = Bloki[2]
# Bloki3 = Bloki[3]

print("Обычный текст:", PT)

# Вывод блочного текста
# print("Обычный текст:", Bloki0, Bloki1, Bloki2, Bloki3)

# Преобразование обычного текста в
# ASCII
PT_Ascii = [ord(x) for x in PT]

# Для блоков текста
# Bloki0_Ascii = [ord(x) for x in Bloki0]
# Bloki1_Ascii = [ord(x) for x in Bloki1]
# Bloki2_Ascii = [ord(x) for x in Bloki2]
# Bloki3_Ascii = [ord(x) for x in Bloki3]

# Преобразование ASCII в
# двоичный формат

PT_Bin = [format(y, '08b') for y in PT_Ascii]
PT_Bin = "".join(PT_Bin)

# Преобразование поблочных тектов
# Bloki0_Bin = [format(y, '08b') for y in Bloki0_Ascii]
# Bloki0_Bin = "".join(Bloki0_Bin)
# Bloki1_Bin = [format(y, '08b') for y in Bloki1_Ascii]
# Bloki1_Bin = "".join(Bloki1_Bin)
# Bloki2_Bin = [format(y, '08b') for y in Bloki2_Ascii]
# Bloki2_Bin = "".join(Bloki2_Bin)
# Bloki3_Bin = [format(y, '08b') for y in Bloki3_Ascii]
# Bloki3_Bin = "".join(Bloki3_Bin)

n = int(len(PT_Bin) // 2)
L1 = PT_Bin[0:n]
R1 = PT_Bin[n::]
m = len(R1)

# Поблочная разбивка, если понадобиться шифровать 4 блока текста
# n = int(len(Bloki0_Bin) // 2)
# n1 = int(len(Bloki1_Bin) // 2)
# n2 = int(len(Bloki2_Bin) // 2)
# n3 = int(len(Bloki3_Bin) // 2)
# L11 = Bloki0_Bin[0:n]
# L12 = Bloki1_Bin[0:n1]
# L13 = Bloki2_Bin[0:n2]
# L14 = Bloki3_Bin[0:n3]
# R11 = Bloki0_Bin[n::]
# R12 = Bloki1_Bin[n1::]
# R13 = Bloki2_Bin[n2::]
# R14 = Bloki3_Bin[n3::]
# m = len(R1)

# Генерируем ключ K1 для
# первого раунда
K1 = rand_key(m)

# Генерируем ключ K2 для
# второго раунда
K2 = rand_key(m)

# Генерируем ключ K3 для
# третьего раунда
K3 = rand_key(m)

# Генерируем ключ K4 для
# четвертого раунда
K4 = rand_key(m)

# первый раунд Фейстеля
f1 = exor(R1, K1)
R2 = exor(f1, L1)
L2 = R1

# Второй раунд Фейстеля
f2 = exor(R2, K2)
R3 = exor(f2, L2)
L3 = R2

# Третий раунд Фейстеля
f3 = exor(R3, K3)
R4 = exor(f3, L3)
L4 = R3

# Четвертый раунд Фейстеля
f4 = exor(R4, K4)
R5 = exor(f4, L4)
L5 = R4

# Шифровать текст
bin_data = L5 + R5
str_data = ' '

for i in range(0, len(bin_data), 7):
    # вырезаем bin_data из диапазона индексов [0, 6]
    # и сохраняем в temp_data
    temp_data = bin_data[i:i + 7]

    # передача temp_data в функцию BinarytoDecimal()
    # чтобы получить десятичное значение соответствующих temp_data
    decimal_data = BinaryToDecimal(temp_data)

    # Декодирование десятичного значения, возвращаемого
    # Функция BinarytoDecimal(), использующая chr()
    # функция, которая возвращает строку, соответствующую
    # символу для заданного значения ASCII и сохранить его
    # в str_data
    str_data = str_data + chr(decimal_data)

print("Шифрованный текст:", str_data)

# Расшифровка
L6 = L5
R6 = R5

f5 = exor(L6, K4)
L7 = exor(R6, f5)
R7 = L6

f6 = exor(L7, K3)
L8 = exor(R7, f6)
R8 = L7

f7 = exor(L8, K2)
L9 = exor(R8, f7)
R9 = L8

f8 = exor(L9, K1)
L10 = exor(R9, f8)
R10 = L9
PT1 = L10 + R10

PT1 = int(PT1, 2)
RPT = binascii.unhexlify('%x' % PT1)
print("Полученный обычный текст: ", RPT)