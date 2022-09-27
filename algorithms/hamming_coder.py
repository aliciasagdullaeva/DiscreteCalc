def calcRedundantBits(m):
    for i in range(m):
        if 2 ** i >= m + i + 1:
            return i


def posRedundantBits(cond, r):
    j = 0
    k = 0
    m = len(cond)
    res = ''

    for i in range(1, m + r + 1):
        if i == 2 ** j:
            res = res + '0'
            j += 1
        else:
            res = res + cond[k]
            k += 1
    return res


def calcParityBits(arr, r):
    n = len(arr)
    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if j & (2 ** i) == (2 ** i):
                val = val ^ int(arr[j-1])
        arr = arr[:(2 ** i) - 1] + str(val) + arr[(2 ** i):]
    return arr


# def expand_and_flip(arr):
#     neg = arr[::-1]
#     res = ''
#     for i in range(len(neg)):
#         res += str(0 ** int(neg[i]))
#     return res

# code = '01110111011'
# m = len(code)
# print(m)
# r = calcRedundantBits(m)
# print(r)
# arr = posRedundantBits(code, r)
# print(arr)
# arr = calcParityBits(arr, r)
# print("Data transferred is " + arr)


def get_hamming_result(cond: str):
    r = calcRedundantBits(len(cond))
    res = posRedundantBits(cond, r)
    res = calcParityBits(res, r)
    return res

