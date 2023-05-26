def is_power_of_two(num):
    power = 0
    while num % 2 == 0 and num > 1:
        num /= 2
        power += 1
    if num == 1:
        return power
    else:
        return None


def pascal_triangle(vector):
    result = []
    vector = list(vector)
    print(vector)
    result.append(vector[0])
    new_vector = []
    while(True):
        new_vector = []
        for i in range(len(vector)-1):
            new_vector.append((int(vector[i])+int(vector[i+1]))%2)
        result.append(new_vector[0])
        # print(new_vector)
        if(len(new_vector)<=1): 
            break
        vector = new_vector
    # print(result)
    return result

def build_zhegalkin_polynomial(vector):
    vector = pascal_triangle(vector)
    n = is_power_of_two(len(vector))  # Длина вектора значений
    variables = ['X' + str(i + 1) for i in range(n)]  # Генерируем список переменных x1, x2, x3, ...

    binary_values = [bin(i)[2:].zfill(n) for i in range(2 ** n)]
    
    monomials = []
    if(vector[0] == 1):
        monomials.append('1')
        polynomial = ' + '.join(monomials)
    for i in range(1,len(binary_values)):
        if vector[i] == 1:
            monomial = ''
            for j in range(n):
                if binary_values[i][j] == '0':
                    continue  # Пропускаем переменные с отрицанием
                monomial += variables[j]
            monomials.append(monomial)

    polynomial = ' + '.join(monomials)  # Сложение всех мономов

    if polynomial.startswith(' + '):
        polynomial = polynomial[3:]  # Удаление первого плюса, если он присутствует без переменных

    return polynomial

# vector = [1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1]
# print(vector)
# print(build_zhegalkin_polynomial(vector))