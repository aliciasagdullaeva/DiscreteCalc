import math


def is_TO(vector):
    return vector[0] == 0


def is_T1(vector):
    return vector[-1] == 1


def is_S(vector):
    n = len(vector)
    for i in range(n // 2):
        if vector[i] == vector[n - i - 1]:
            return False
    return True


def is_sheffer_function(vector):
    print(vector)
    print(is_TO(vector))
    print(is_T1(vector))
    print(is_S(vector))
    print(not is_TO(vector) and not is_T1(vector) and not is_S(vector))
    return not is_TO(vector) and not is_T1(vector) and not is_S(vector)

    # Проверка M (монотонность)

    # Проверка L (линейность) не применима к функциям Шеффера, так как они всегда нелинейны

    return True


