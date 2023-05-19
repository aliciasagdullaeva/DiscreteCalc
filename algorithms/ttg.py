import itertools
import re
from distutils.util import strtobool

import pyparsing

# dict of boolean operations
OPERATIONS = {
    'not': (lambda x: not x),
    '-': (lambda x: not x),
    '~': (lambda x: not x),

    'or': (lambda x, y: x or y),
    'nor': (lambda x, y: not (x or y)),
    'xor': (lambda x, y: x != y),

    'and': (lambda x, y: x and y),
    'nand': (lambda x, y: not (x and y)),

    '=>': (lambda x, y: (not x) or y),
    'implies': (lambda x, y: (not x) or y),

    '=': (lambda x, y: x == y),
    '!=': (lambda x, y: x != y),
}


def replace_boolean_operators(expr):
    # Add "and" between variables written together
    expr = re.sub(r'([a-zA-Z][0-9])(?=[a-zA-Z][0-9])', r'\1 ∧ ', expr)

    # Add "and" between a variable and a negation
    expr = re.sub(r'([a-zA-Z][0-9])¬', r'\1 ∧ ¬', expr)


    mapping = {
        '∧': ' and ',
        '∨': ' or ',
        '¬': ' not ',
        '→': ' implies ',
        '↔': ' = ',
        '↓': ' nand ',
        '|': ' nor ',
        '⊕': ' xor '
    }

    for key, value in mapping.items():
        expr = expr.replace(key, value)

    expr = ' '.join(expr.split())
    return expr


def get_unique_variables(phrase):
    """
    Функция для получения уникальных переменных из строки, исключая заданные операции.
    """

    # Находим все переменные с использованием регулярного выражения
    variables = re.findall(r"[A-Za-z]+\d*", phrase)

    # Отфильтровываем переменные, исключая заданные операции
    filtered_variables = [var for var in variables if var.lower() not in OPERATIONS.keys()]

    # Получаем уникальные переменные, преобразуя список в множество и затем обратно в список
    unique_variables = list(set(filtered_variables))

    unique_variables.sort()

    return unique_variables


def recursive_map(func, data):
    """Recursively applies a map function to a list and all sublists."""
    if isinstance(data, list):
        return [recursive_map(func, elem) for elem in data]
    else:
        return func(data)


def string_to_bool(string):
    """Converts a string to boolean if string is either 'True' or 'False'
    otherwise returns it unchanged.
    """

    try:
        string = bool(strtobool(string))
    except ValueError:
        pass
    return string


def solve_phrase(phrase):
    """Recursively evaluates a logical phrase that has been grouped into
    sublists where each list is one operation.
    """
    if isinstance(phrase, bool):
        return phrase
    if isinstance(phrase, list):
        # list with just a list in it
        if len(phrase) == 1:
            return solve_phrase(phrase[0])
        # single operand operation
        if len(phrase) == 2:
            return OPERATIONS[phrase[0]](solve_phrase(phrase[1]))
        # double operand operation
        else:
            return OPERATIONS[phrase[1]](
                solve_phrase(phrase[0]),
                solve_phrase([phrase[2]])
            )


def group_operations(phrase):
    """Recursively groups logical operations into separate lists based on
    the order of operations such that each list is one operation.

    Order of operations is:
        not, and, or, implication
    """
    if isinstance(phrase, list):
        for operator in ['not', '~', '-']:
            while operator in phrase:
                index = phrase.index(operator)
                phrase[index] = [operator, group_operations(phrase[index + 1])]
                phrase.pop(index + 1)
        for operator in ['and', 'nand']:
            while operator in phrase:
                index = phrase.index(operator)
                phrase[index] = [group_operations(phrase[index - 1]),
                                 operator,
                                 group_operations(phrase[index + 1])]
                phrase.pop(index + 1)
                phrase.pop(index - 1)
        for operator in ['or', 'nor', 'xor']:
            while operator in phrase:
                index = phrase.index(operator)
                phrase[index] = [group_operations(phrase[index - 1]),
                                 operator,
                                 group_operations(phrase[index + 1])]
                phrase.pop(index + 1)
                phrase.pop(index - 1)
    return phrase


class Truths:
    """
    Class Truhts with modules for table formatting, valuation and CLI
    """

    def __init__(self, phrase: str, bases=None, ints=True, ascending=True):
        self.phrase = phrase
        self.ints = ints

        # Get variables
        self.bases = bases or get_unique_variables(phrase)

        # generate the sets of booleans for the bases
        if ascending:
            order = [False, True]
        else:
            order = [True, False]

        self.base_conditions = list(
            itertools.product(
                order,
                repeat=len(self.bases)
            )
        )

        # regex to match whole words defined in self.bases
        # used to add object context to variables in self.phrase
        self.p = re.compile(r'(?<!\w)(' + '|'.join(self.bases) + r')(?!\w)')

        # used for parsing logical operations and parenthesis
        self.to_match = pyparsing.Word(pyparsing.alphanums)
        for item in itertools.chain(
                self.bases,
                [key for key, val in OPERATIONS.items()]
        ):
            self.to_match |= item
        self.parens = pyparsing.nestedExpr('(', ')', content=self.to_match)

    def calculate(self, *args):
        """
        Evaluates the logical value for each expression
        """
        bools = dict(zip(self.bases, args))

        # substitute bases in phrase with boolean values as strings
        phrase = self.p.sub(lambda match: str(bools[match.group(0)]), self.phrase)  # NOQA long line
        # wrap phrase in parens
        phrase = '(' + phrase + ')'
        # parse the expression using pyparsing
        interpreted = self.parens.parseString(phrase).asList()[0]
        # convert any 'True' or 'False' to boolean values
        interpreted = recursive_map(string_to_bool, interpreted)
        # group operations
        interpreted = group_operations(interpreted)
        # evaluate the phrase

        # add the bases and evaluated phrases to create a single row
        result = solve_phrase(interpreted)
        if self.ints:
            result = int(result)
        return result

    def value_vector(self):
        result = []
        for conditions_set in self.base_conditions:
            result.append(self.calculate(*conditions_set))
        print(result)
        return result


def get_value_vector(expr):
    phrase = replace_boolean_operators(expr)
    return Truths(phrase).value_vector()
