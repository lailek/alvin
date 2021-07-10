import utilities

def a_add(row,start_row=0,a="a",b="b",c="c"):
    aa = utilities.col2num(a)
    bb = utilities.col2num(b)
    cc = utilities.col2num(c)
    return row[aa] + row[bb] + row[cc]

def b_multiply(row,start_row=0,alvin="a",daniel="b",albert="c"):
    aa = utilities.col2num(alvin)
    cc = utilities.col2num(albert)
    return row[aa] * row[cc]

def c_check(row,start_row=0,alvin="a",albert="c"):
    aa = utilities.col2num(alvin)
    cc = utilities.col2num(albert)
    if row[aa] > 1:
        return "alvin"
    else:
        return "albert"
    #return row[aa] * row[cc]