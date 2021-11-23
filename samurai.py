import csv

def cross(A, B, c=''):
    "Cross product of elements in A and elements in B."
    return [a+b+c for a in A for b in B]


digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits

id_var = 'a'
square_a = cross(rows, cols, id_var)
unitlist_a = ([cross(rows, c, id_var) for c in cols] +
              [cross(r, cols, id_var) for r in rows] +
              [cross(rs, cs, id_var) for rs in ('ABC', 'DEF', 'GHI')
               for cs in ('123', '456', '789')])

id_var = 'b'
square_b = cross(rows, cols, id_var)
unitlist_b = ([cross(rows, c, id_var) for c in cols] +
              [cross(r, cols, id_var) for r in rows] +
              [cross(rs, cs, id_var) for rs in ('ABC', 'DEF', 'GHI')
               for cs in ('123', '456', '789')])

id_var = 'c'
square_c = cross(rows, cols, id_var)
unitlist_c = ([cross(rows, c, id_var) for c in cols] +
              [cross(r, cols, id_var) for r in rows] +
              [cross(rs, cs, id_var) for rs in ('ABC', 'DEF', 'GHI')
               for cs in ('123', '456', '789')])

id_var = 'd' 
square_d = cross(rows, cols, id_var)
unitlist_d = ([cross(rows, c, id_var) for c in cols] +
              [cross(r, cols, id_var) for r in rows] +
              [cross(rs, cs, id_var) for rs in ('ABC', 'DEF', 'GHI')
               for cs in ('123', '456', '789')])

def repl(c):
    a = b = 0
    s = ""
    if c[0] in 'ABCGHI' and c[1] in '123789':
        if c[0] in 'ABC':
            s += chr(ord(c[0]) + 6)
            a = 1
        elif c[0] in 'GHI':
            s += chr(ord(c[0]) - 6)
            a = 2
        if c[1] in '123':
            s += chr(ord(c[1]) + 6)
            b = 1
        elif c[1] in '789':
            s += chr(ord(c[1]) - 6)
            b = 2
    else:
        return c
    if a == 1 and b == 1:
        s += 'a'
    elif a == 1 and b == 2:
        s += 'b'
    elif a == 2 and b == 1:
        s += 'c'
    elif a == 2 and b == 2:
        s += 'd'
    return s


id_var = '+'
square_mid = [repl(x) for x in cross(rows, cols, id_var)]
unitlist_mid = ([square_mid[x*9:x*9+9] for x in range(0, 9)] +
                [square_mid[x::9] for x in range(0, 9)] +
                [cross(rs, cs, id_var) for rs in ('ABC', 'DEF', 'GHI')
                 for cs in ('123', '456', '789')
                 if not (rs in 'ABCGHI' and cs in '123789')])

all_squares = set(square_a + square_b + square_c + square_d + square_mid)
all_unitlists = unitlist_a + unitlist_b + \
    unitlist_c + unitlist_d + unitlist_mid

units = dict((s, [u for u in all_unitlists if s in u])
             for s in all_squares)
peers = dict((s, set(sum(units[s], []))-set([s]))
             for s in all_squares)


def parse_grid_samurai(grid):
    values = dict((s, digits) for s in all_squares)
    for s, d in grid_values(grid).items():
        if d in digits and not assign(values, s, d):
            return False
    return values
   
def write_points_to_database(name, counter):
    writer = csv.writer(open(name, 'w'))
    writer.writerow(['Column and Digit', 'State' , 'Numbers'])
    for key, value in counter.items():
        writer.writerow([key[0]+ key[1], key[2], value])

def flatten(arr):
    return [x for sub in arr for x in sub]


def grid_values(grid):
    a = flatten([x[:9] for x in grid[:9]])
    b = flatten([x[12:] for x in grid[:9]])
    c = flatten([x[:9] for x in grid[12:]])
    d = flatten([x[12:] for x in grid[12:]])
    mid = flatten([x[6:15] for x in grid[6:15]])
    chars = a + b + c + d + mid
    sqrs = square_a + square_b + square_c + square_d + square_mid
    assert len(chars) == 405
    return dict(zip(sqrs, chars))

def assign(values, s, d):
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False


def eliminate(values, s, d):
    if d not in values[s]:
        return values
    values[s] = values[s].replace(d, '')
    if len(values[s]) == 0:
        return False
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]]
        if len(dplaces) == 0:
            return False
        elif len(dplaces) == 1:
            if not assign(values, dplaces[0], d):
                return False
    return values


def display(values, sqr):
    width = 1+max(len(values[s]) for s in sqr)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[sqr[(ord(r) - 65) * 9 + int(c) - 1]]
                      .center(width)+('|' if c in '36' else '') for c in cols))
        if r in 'CF':
            print(line)
    print()


def display_samurai(vals):
    if not vals:
        print("Solution not found, please check if test is valid.")
        return
    print("Top left:")
    display(vals, square_a)
    print("Top right:")
    display(vals, square_b)
    print("Bottom left:")
    display(vals, square_c)
    print("Bottom right:")
    display(vals, square_d)
    print("Middle:")
    display(vals, square_mid)


def solve(grid):
    return search(parse_grid_samurai(grid))


def search(values):
    if values is False:
        return False
    if all(len(values[s]) == 1 for s in all_squares):
        write_points_to_database("PointsSuccess.csv",values)
        return values
    write_points_to_database("Points.csv",values)
    n, s = min((len(values[s]), s) for s in all_squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d))
                for d in values[s])


def some(seq):    
    for e in seq:
        if e:
            return e
    return False

def solved(values):
    def unitsolved(unit):
        return set(values[s] for s in unit) == set(digits)
    return values is not False and all(unitsolved(unit) for unit in all_unitlists)


def changeTextFileFormat(file):
    newFile = file.read().replace("*", "0")
    k=0
    for i in range(1, 13, 2):
        newFile = newFile[:(i*9)+k]+"..."+newFile[(i*9)+k:]
        k+=4
    k+=3    
    newFile = newFile[:198]+"......"+newFile[198:]
    newFile = newFile[:213]+"......"+newFile[213:]
    newFile = newFile[:220]+"......"+newFile[220:]
    newFile = newFile[:235]+"......"+newFile[235:]
    newFile = newFile[:242]+"......"+newFile[242:]
    newFile = newFile[:257]+"......"+newFile[257:]
    m=6
    for j in range(37, 49, 2):
        newFile = newFile[:(j*9)+m]+"..."+newFile[(j*9)+m:]
        m+=4

    newFile=newFile.split('\n')
    return newFile


if __name__ == '__main__':
    f = open(r"C:\Users\z004d20z\Desktop\Programlama\Python\SamuraiSudoku\SamuraiSudokuSolver\tests\easy1.txt", 'r')
    f=changeTextFileFormat(f)
    samurai_grid = f
    ans = solve(samurai_grid)
    display_samurai(ans)
