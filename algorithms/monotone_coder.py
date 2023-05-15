import math


# Функция is_monotonic проверяет монотонность булевой функции, сравнивая значения функции для всех пар входных
# значений. Если значение функции для меньшего входного значения больше, чем значение для большего входного значения,
# то функция не является монотонной и возвращает False. В противном случае функция возвращает True.

def is_monotonic(vector):
    n = len(vector)
    num_vars = int(math.log2(n))

    for i, value1 in enumerate(vector[:-1]):
        for j, value2 in enumerate(vector[i + 1:]):
            i_bin = bin(i)[2:].zfill(num_vars)
            j_bin = bin(i + j + 1)[2:].zfill(num_vars)
            if all(a <= b for a, b in zip(i_bin, j_bin)) and value1 > value2:
                return False

    return True
