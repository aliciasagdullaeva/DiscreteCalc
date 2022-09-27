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
    n = 0
    k = cond.count("∨") + 1
    vars = {"X": 0, "Y": 0, "Z": 0, "T": 0}
    for key, value in vars.items():
        if cond.count(key):
            vars[key] = cond.count(key)
            n += 1
    result = str(n) + " " + str(k) + "\n"

    var_pos = [key for key, value in vars.items() if value]
    conjuctions = cond.split('∨')
    dnf = []

    for con in conjuctions:
        line = ['*'] * n
        neg = False
        for i in con:
            if i == '¬':
                neg = True
                continue
            if i in var_pos:
                if not neg:
                    line[var_pos.index(i)] = "1"
                else:
                    line[var_pos.index(i)] = "0"
                neg = False
        dnf.append(line.copy())

    for line in dnf:
        for symbol in line:
            result += symbol
        result += "\n"

    return result


def convert_answer(tupik_dnfs: list, n: int, k: int, cond: str):
    n = 0
    vars = {"X": 0, "Y": 0, "Z": 0, "T": 0}
    for key, value in vars.items():
        if cond.count(key):
            vars[key] = cond.count(key)
            n += 1
    var_pos = [key for key, value in vars.items() if value]
    result = []
    for tupik in tupik_dnfs:
        dnf = ""
        for line in tupik:
            for i, element in enumerate(line):
                if element == "1":
                    dnf += var_pos[i]
                elif element == "0":
                    dnf += "¬" + var_pos[i]
            dnf += "∨"
        result.append(dnf[:-1])
    return result




def get_TDNF_result(cond: str):
    a = reformat_cond(cond)
    a = a.replace('\n', ' ', 1).replace('\n', '').split(' ')
    dnf, n, k = parse_dnf(a)
    base_vector = find_vector(dnf, n)
    all_shorts = create_all_short_dnfs(dnf, k)
    all_shorts.sort(key=len)
    minimal_dnfs = find_minimal_dnfs(all_shorts, n, base_vector)
    tupik_dnfs = get_tupik_dnfs(minimal_dnfs)
    result = convert_answer(tupik_dnfs, n, k, cond)
    return result
