import math
import itertools


class ArgumentError(Exception):
    title = 'argument error'
    msg = ''

    def init(self, msg):
        self.msg = msg


def convert_to_2(number):
    arr = []
    if number == 1 or number == 0:
        return [number]
    result = number
    while result != 1:
        rem = result % 2
        result = int(result / 2)
        arr.append(rem)
        if result == 1:
            arr.append(result)

    return arr


def build_g_matrix(m, sigma):
    n = pow(2, m)
    G = list()
    G.append([1 for i in range(n)])
    for i in range(m):
        G.append([0 for i in range(n)])

    for i in range(n):
        number_2 = convert_to_2(i)
        for k in range(len(number_2)):
            G[k + 1][i] = number_2[k]

    comb = itertools.combinations(G[1:], sigma)
    for i in comb:
        arr = []
        for j in range(n):
            arr.append(i[0][j] * i[1][j])
        G.append(arr)

    return G


def get_uk(G, m, sigma):
    ucount = 1 + m + math.comb(m, sigma)
    n = pow(2, m)
    U = list()
    for i in range(n):
        arr = []
        for j in range(ucount):
            if G[j][i] == 1:
                arr.append(j)
        U.append(arr)
    return U


def rm_code(code, m, sigma):
    if m < 3:
        raise ArgumentError('«m» cannot be less than 3')
    if sigma > m or sigma < 2:
        raise ArgumentError('Sigma cannot be less than «m» and greater than «2»')

    count = 1 + m + math.comb(m, sigma)
    if len(code) != count:
        raise ArgumentError(f'Wrong code length. If «m» is {m} then code length must be {count}')

    G = build_g_matrix(m, sigma)
    U = get_uk(G, m, sigma)

    arr = []
    for i in range(len(U)):
        res = 0
        for j in U[i]:
            res += code[j]
        arr.append(res % 2)
    return arr, G
