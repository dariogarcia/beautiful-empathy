SMALL_SQUARE = 's'
BIG_SQUARE = 'S'

def gets_new_color(hits,owned):
    if owned < 4:
        return True
    elif hits==0:
        return False
    else:
        return owned < hits+4

def gets_shape(hits,owned):
    if owned < 4:
        if hits < 2:
            return {SMALL_SQUARE:2}
        elif hits < 4:
            return {SMALL_SQUARE:4}
        else:
            return {SMALL_SQUARE:2,BIG_SQUARE:1}
    elif owned < 8:
        if hits < 2:
            return {BIG_SQUARE:2}
        elif hits < 4:
            return {SMALL_SQUARE:2,BIG_SQUARE:2}
        else:
            return {SMALL_SQUARE:4,BIG_SQUARE:2}
    else:
        if hits < 2:
            return {BIG_SQUARE:4}
        elif hits < 4:
            return {SMALL_SQUARE:4,BIG_SQUARE:4}
        else:
            return {SMALL_SQUARE:8,BIG_SQUARE:4}
        

