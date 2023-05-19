from .ttg import get_value_vector


def check_equivalence(expr1, expr2):
    vector1 = get_value_vector(expr1)
    vector2 = get_value_vector(expr2)

    print(vector1)
    print(vector2)

    if vector1 != vector2:
        return False

    return True


