import re


def scan_dnf(file_path: str):
    f = open(file_path, 'r')
    a = f.read()
    f.close()
    a = a.replace('\n', ' ', 1).replace('\n', '').split(' ')
    return a


def parse_dnf(a: list):
    n = int(a[0])
    k = int(a[1])
    s = a[2]
    dnf = []
    line = []  # conjunction
    for i in range(k):
        for j in range(n):
            line.append(s[j + (i * n)])
        dnf.append(line.copy())
        line.clear()
    return dnf, n, k


def bool_up(line: list, n: int):
    for x in range(n - 1, -1, -1):
        if line[x] == 0:
            line[x] = 1
            break
        else:
            line[x] = 0


def create_truth_table(n: int):
    truth_table = []
    line = []
    for i in range(n):
        line.append(0)
    for i in range(2 ** n):
        truth_table.append(line.copy())
        bool_up(line, n)
    return truth_table


def find_vector(dnf: list, n: int):
    vector = []
    truth_table = create_truth_table(n)
    for line in truth_table:
        disjunction = 0
        for part in dnf:
            conjunction = 1
            for i, x in enumerate(part):
                if x == '1':
                    conjunction &= line[i]
                elif x == '0':
                    conjunction &= 0 ** line[i]
                elif x == '*':
                    continue
            disjunction |= conjunction
        vector.append(disjunction)
    return vector


def create_all_short_dnfs(dnf: list, k: int):
    combination = [0] * k
    all_short_dnfs = []
    bool_up(combination, k)
    for c in range(2 ** k - 2):
        short_dnf = []
        for i, conj in enumerate(combination):
            if conj == 1:
                short_dnf.append(dnf[i])
        all_short_dnfs.append(short_dnf.copy())
        bool_up(combination, k)
    return all_short_dnfs


def is_same(vector: list, base_vector: list):
    for i, element in enumerate(base_vector):
        if element != vector[i]:
            return False
    return True


def find_minimal_dnfs(dnfs: list, n: int, base_vector: list):
    minimal_dnfs = []
    for dnf in dnfs:
        vector = find_vector(dnf, n)
        if is_same(vector, base_vector):
            minimal_dnfs.append(dnf.copy())
    return minimal_dnfs


def has_more_minimal(dnf: list, tupik_dnfs: list):
    is_included = True
    for tupik in tupik_dnfs:
        for part in tupik:
            if part not in dnf:
                is_included = False
                break
        if is_included:
            return True
    return False


def get_tupik_dnfs(dnfs: list):
    tupik_dnfs = []
    for dnf in dnfs:
        if not (has_more_minimal(dnf, tupik_dnfs) or dnf in tupik_dnfs):
            tupik_dnfs.append(dnf.copy())
    return tupik_dnfs


def reformat_cond(cond: str):
    k = cond.count("∨") + 1
    n = int(max(re.findall('[0-9]+', cond)))
    result = f"{n} {k}\n"
    lines = [line.split("∧") for line in cond.split("∨")]
    for line in lines:
        line = [x[::-1].replace("X", "") for x in line]
        line.sort()

        # diff = n - len(line)
        # if len(line) < n:
        #     for i in range(len(line)):
        #         if str(i + 1) not in line[i]:
        #             line.insert(i, "")
        #     if str(n) not in line[-1]:
        #         line.append("")

        mask = ['*'] * n
        for i, x in enumerate(line):
            mask[int(x[0]) - 1] = '0' if '¬' in x else '1'
        str_line = ""
        result += str_line.join([m for m in mask])
        result += '\n'

        # for i, x in enumerate(mask, start=1):
        #     if str(i) in x and "¬" not in x:
        #         result += '1'
        #     elif str(i) in x and "¬" in x:
        #         result += '0'
        #     else:
        #         result += '*'

    return result


def convert_answer(tupik_dnfs: list, n: int, k: int, cond: str):
    result = []
    for dnf in tupik_dnfs:
        string = ""
        for i, line in enumerate(dnf):
            for j, x in enumerate(line, start=1):
                if '1' in x:
                    string += f"X{j}"
                elif '0' in x:
                    string += f"¬X{j}"
                elif '*' in x:
                    continue
                else:
                    raise ValueError

                string += '∧'

            string = string[:-1] + '∨'

        result.append(string[:-1])
    return result




def get_TDNF_result(cond: str): # cond = 'XY∨¬X∨Y'
    a = reformat_cond(cond) # a = '2 3\n11\n0*\n*1\n'
    a = a.replace('\n', ' ', 1).replace('\n', '').split(' ') # a = ['2', '3', '110**1']
    dnf, n, k = parse_dnf(a) # dnf = [['1', '1'], ['0', '*'], ['*', '1']]
    base_vector = find_vector(dnf, n) # base_vector = [1, 1, 0, 1]
    all_shorts = create_all_short_dnfs(dnf, k) # all_shrots = [[['*', '1']], [['0', '*']], [['0', '*'], ['*', '1']], [['1', '1']], [['1', '1'], ['*', '1']], [['1', '1'], ['0', '*']]]
    all_shorts.sort(key=len)
    minimal_dnfs = find_minimal_dnfs(all_shorts, n, base_vector) # minimal_dnfs = [[['0', '*'], ['*', '1']], [['1', '1'], ['0', '*']]]
    tupik_dnfs = get_tupik_dnfs(minimal_dnfs) # tupik_dnfs = [[['0', '*'], ['*', '1']], [['1', '1'], ['0', '*']]]
    if len(tupik_dnfs):
        result = convert_answer(tupik_dnfs, n, k, cond) # result = ['¬X∨Y', 'XY∨¬X']
    else:
        result = convert_answer([dnf], n, k, cond)
    return result
