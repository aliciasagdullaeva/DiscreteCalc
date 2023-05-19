import re


def parse_dnf(expr):
    # разделяем строку на отдельные конъюнкты
    conjuncts_str = expr.split('∨')

    conjuncts = []
    for conjunct_str in conjuncts_str:
        conjunct = []
        # находим все переменные и их отрицания
        for var in re.findall(r'(¬?[a-z][0-9]*)', conjunct_str):
            if var.startswith('¬'):
                conjunct.append((var[1:], False))
            else:
                conjunct.append((var, True))
        conjuncts.append(conjunct)

    return conjuncts


def conjuncts_to_string(conjuncts):
    conjuncts_str = []

    for conjunct in conjuncts:
        conjunct_str = []
        for var, neg in conjunct:
            if neg:
                conjunct_str.append(var)
            else:
                conjunct_str.append('¬' + var)
        conjuncts_str.append(''.join(conjunct_str))

    result = '∨'.join(conjuncts_str)

    return result


def blake_poretsky_algorithm(conjuncts):
    # convert each conjunct (list of variables) into a frozenset
    conjuncts = [frozenset(c) for c in conjuncts]
    # start with the initial conjuncts
    Q = set(conjuncts)
    R = set()
    while Q:
        P = Q.copy()
        Q.clear()
        for Y in P:
            # check if there exists a conjunct in R that is a subset of Y
            for Z in R:
                if Z.issubset(Y):
                    break
            else:  # no break, i.e., no such Z exists
                # find all conjuncts in P that are disjoint with Y
                D = {Z for Z in P if not any(x in Y for x in Z)}
                # add Y to the new set of conjuncts
                R.add(Y)
                # add the difference between Y and each conjunct in D to Q
                Q.update({Y - Z for Z in D})
    return R


def get_SokrDNF_result(cond: str):  # cond = 'XY∨¬X∨Y'
    conjuncts = parse_dnf(cond)
    sokr_dnf = blake_poretsky_algorithm(conjuncts)

    return conjuncts_to_string(sokr_dnf)


# Пример использования функции
expr = "¬x1¬x2∨¬x1x3∨x1x2∨x1¬x3∨¬x2¬x3∨x2x3"
# print(get_SokrDNF_result(expr))
