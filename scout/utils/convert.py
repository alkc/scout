def isfloat(x):
    try:
        a = float(x)
    except ValueError:
        return False
    else:
        return True


def isint(x):
    try:
        a = float(x)
        b = int(a)
    except ValueError:
        return False
    else:
        return a == b


def make_bool_pass_none(string):
    if str(string).lower() == "none":
        return None
    return make_bool(string)


def make_bool(string):
    """Convert a string to boolean"""
    if str(string).lower() in ["yes", "true", "1", "t"]:
        return True
    return False


def convert_number(string):
    """Convert a string to number
    If int convert to int otherwise float

    If not possible return None
    """
    res = None
    if isint(string):
        res = int(float(string))
    elif isfloat(string):
        res = float(string)
    return res


def convert_aa_3_to_1(string):
    aa_3_to_1 = {
        "Ala": "A",
        "Arg": "R",
        "Asn": "N",
        "Asp": "D",
        "Asx": "B",
        "Cys": "C",
        "Glu": "E",
        "Gln": "Q",
        "Glx": "Z",
        "Gly": "G",
        "His": "H",
        "Ile": "I",
        "Leu": "L",
        "Lys": "K",
        "Met": "M",
        "Phe": "F",
        "Pro": "P",
        "Ser": "S",
        "Thr": "T",
        "Trp": "W",
        "Tyr": "Y",
        "Val": "V",
    }
    return aa_3_to_1.get(string, None)
