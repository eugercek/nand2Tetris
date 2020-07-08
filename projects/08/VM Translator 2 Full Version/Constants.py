class Constants:
    C_ARITHMETIC = 0
    C_PUSH       = 1
    C_POP        = 2

    EMPTY_LINE = 0
    COMMENT_LINE = 0
    NOT_COMMAND = 0

    NO_DEBUG = 0

    # Segment names
    SEGMENTS={
    'local':"LCL",
    'argument':"ARG",
    'this':"THIS",
    'that':"THAT",
    'temp':5,
    'static':16,
    "pointer":{0:"THIS",1:"THAT"},
    }

    JUMPS={
        "eq":"JEQ",
        "gt":"JGT",
        "lt":"JLT"
    }
