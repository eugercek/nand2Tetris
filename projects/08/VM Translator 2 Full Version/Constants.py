class Constants:
    C_ARITHMETIC = 0
    C_PUSH       = 1
    C_POP        = 2
    C_LABEL      = 3
    C_GOTO       = 4
    C_IF         = 5
    C_FUNCTION   = 6
    C_RETURN     = 7
    C_CALL       = 8

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
