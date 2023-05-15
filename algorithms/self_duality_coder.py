def is_S(vector):
    # Проверка S (самодвойственность)
    n = len(vector)
    for i in range(n // 2):
        if vector[i] == vector[n - i - 1]:
            return False
    return True
