import math

from alphabet import Alphabet, Vowels


def cvcv(val) -> str:
    result = ""
    for v in val:
        num_val = Alphabet[v].value
        if is_S(v):
            result += v
        else:
            result += get_c(num_val)
            result += get_v(num_val)
    return result


def ccvc(val) -> str:
    result = ""
    prev = ""
    for v in val:
        if is_S(v):
            result += v
            prev = ""
        elif prev == "":
            prev = v
        elif prev != "" and is_V(v):
            result += cv_merger(prev, v)
            prev = ""
        elif prev != "" and not is_V(v):
            result += prev
            prev = v
    return result + prev


def is_C(val) -> bool:
    if (val + 1) % 7 == 0:
        return True
    return False


def is_V(val) -> bool:
    try:
        _ = Vowels[val].value
        return True
    except KeyError as e:
        return False


def is_S(val) -> bool:
    num_val = Alphabet[val].value
    return 278 >= num_val > 231


def get_c(val) -> str:
    c_num = math.ceil(val / 7) * 7 - 1
    return Alphabet(c_num).name


def get_v(val) -> str:
    x = val % 7
    return Vowels(x).name


def cv_merger(c, v) -> str:
    v_num = Vowels[v].value
    c_num = Alphabet[c].value
    c_floor = math.floor(c_num / 7)
    if v_num == 0:
        res = Alphabet((c_floor * 7) + 7).name
    else:
        res = Alphabet((c_floor * 7) + v_num).name
    return res
