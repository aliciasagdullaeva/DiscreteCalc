import itertools
import re


def all_combinations(variables):
    return list(itertools.product([False, True], repeat=len(variables)))


def parse_literal(literal):
    negated = literal.startswith("¬")
    variable = literal[1:] if negated else literal
    return variable, not negated


def parse_clause(clause):
    literals = re.findall(r"(¬?[A-Za-z]\d*)", clause)
    return [parse_literal(literal) for literal in literals]


def parse_dnf(expr):
    clauses = expr.split("∨")
    return [parse_clause(clause) for clause in clauses]


def extract_variables(expr):
    variables = re.findall(r'[A-Za-z]\d*', expr)
    return sorted(list(set(variables)))


def eval_dnf(expr, variable_values):
    dnf = parse_dnf(expr)
    result = []
    for clause in dnf:
        clause_value = True
        for variable, positive in clause:
            if positive:
                clause_value &= variable_values[variable]
            else:
                clause_value &= not variable_values[variable]
        result.append(clause_value)
    return result


def dnf_vector(expr):
    variables =extract_variables(expr)
    combinations = all_combinations(variables)
    vector = []
    for combination in combinations:
        variable_values = dict(zip(variables, combination))
        vector.append(any(eval_dnf(expr, variable_values)))
    return vector


# Пример использования
# expr = "X4X2∨¬X1X3∨¬X2X3"
#
# vector = dnf_vector(expr)
# print(vector)
