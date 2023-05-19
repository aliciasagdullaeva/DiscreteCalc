from itertools import chain, combinations

from .ttg import get_value_vector


def get_all_subsets(dnf):
    return list(chain(*map(lambda x: combinations(dnf, x), range(0, len(dnf) + 1))))


def division_of_conjuncts(dnf):
    return [x.strip() for x in dnf.split('∨')]


def union_of_conjuncts(dnf):
    return '∨'.join(dnf)


def get_TDNF_result(dnf):
    dnf = division_of_conjuncts(dnf)
    all_subsets = get_all_subsets(dnf)
    base_vector = get_value_vector(union_of_conjuncts(dnf))

    tupikovye_dnfs = []

    for subset in all_subsets:
        if subset:
            if get_value_vector(union_of_conjuncts(subset)) == base_vector:
                tupikovye_dnfs.append(list(subset))

    final_tupikovye_dnfs = []

    for dnf1 in tupikovye_dnfs:
        is_tupikovaya = True
        for dnf2 in tupikovye_dnfs:
            if set(dnf2).issubset(set(dnf1)) and dnf1 != dnf2:
                is_tupikovaya = False
                break
        if is_tupikovaya:
            final_tupikovye_dnfs.append(union_of_conjuncts(dnf1))

    return final_tupikovye_dnfs

# mapping = {
#     '∧': ' and ',
#     '∨': ' or ',
#     '¬': ' not ',
#     '→': ' implies ',
#     '↔': ' = ',
#     '↓': ' nand ',
#     '|': ' nor ',
#     '⊕': ' xor '
# }
#
# "¬x1x2∨¬x1x3"
# "x1∨¬x2∨x3"
# "x1x2∨x1¬x3∨x1x4∨x2x3∨x2¬x4∨x3x4"
# "x1¬x2∨x1¬x3∨x1x4∨¬x2x3∨x2¬x3∨x3x4"
# "¬x1¬x2∨¬x1x3∨x1x2∨x1¬x3∨¬x2¬x3∨x2x3"
#
# print(get_TDNF_result("x1∨¬x2∨x3"))
