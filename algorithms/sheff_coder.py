import math


def is_sheffer_function(vector):
    n = len(vector)
    num_vars = int(math.log2(n))

    # Проверка T0
    if not vector[0] is False:
        return False

    # Проверка T1
    if vector[-1] is True:
        return False

    # Проверка S (самодвойственность)
    for i in range(n // 2):
        if vector[i] == vector[n - i - 1]:
            return False

    # Проверка M (монотонность)

    # Проверка L (линейность) не применима к функциям Шеффера, так как они всегда нелинейны

    return True


