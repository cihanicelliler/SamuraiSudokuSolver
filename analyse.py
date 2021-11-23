import samurai
import math
import csv
from Ticker import *
from samurai import *

from sudoku import *
from collections import Counter

def samurai_puzzle():
    
    f = open(r"C:\Users\z004d20z\Desktop\Programlama\Python\SamuraiSudoku\SamuraiSudokuSolver\tests\easy1.txt", 'r')
    samurai_grid=changeTextFileFormat(f)
    grid_a=""
    grid_b=""
    grid_c=""
    grid_d=""
    grid_plus=""
    for i in range(0,9):
        grid_a=grid_a+samurai_grid[i][:9]
        grid_b=grid_b+samurai_grid[i][12:21]
    for i in range(12,21):
        grid_c=grid_c+samurai_grid[i][:9]
        grid_d=grid_d+samurai_grid[i][12:21]
    for i in range(6,15):
        grid_plus=grid_plus+samurai_grid[i][6:15]
    grid_a=grid_a.replace('0','.')
    grid_b=grid_b.replace('0','.')
    grid_c=grid_c.replace('0','.')
    grid_d=grid_d.replace('0','.')
    grid_plus=grid_plus.replace('0','.')
    
    init_square_count = {}
    for s in squares:
        init_square_count[s] = 0
    counts = {}
    counts['a'] = count_initialized_squares(grid_a, init_square_count.copy())
    counts['b'] = count_initialized_squares(grid_b, init_square_count.copy())
    counts['c'] = count_initialized_squares(grid_c, init_square_count.copy())
    counts['d'] = count_initialized_squares(grid_d, init_square_count.copy())
    counts['+'] = count_initialized_squares(grid_plus, init_square_count.copy())

    return samurai_grid, counts


################ Puzzle Helpers ################

square_indices_map = {} # Lazy map of square indices
index_squares_map = {} # Lazy map of index squares

def index_to_square(index):
    if index not in index_squares_map:
        index_squares_map[index] = chr(math.floor(index/9)+ord('A')) + str(index%9+1)
    return index_squares_map[index]

def count_initialized_squares(grid, count_map):
    for i in range(len(grid)):
        if grid[i] != '.':
            count_map[index_to_square(i)] += 1
    return count_map

################ Data Handlers ################

def write_counter_to_database(name, counter):
    writer = csv.writer(open(name, 'w'))
    writer.writerow(['Y-Axis', 'X-Axis' , 'Number of Hits'])
    for key, value in counter.items():
        writer.writerow([key[0], key[1] , value])


################ Testing ################

# Initialize Counters for each Sudoku grid 
a = Counter()
b = Counter()
c = Counter()
d = Counter()
plus = Counter()

if __name__ == '__main__':
    success_counter = 0
    samurai_grid, counts = samurai_puzzle()
    ans = samurai.solve(samurai_grid)
    if ans:
        success_counter += 1
        a.update(counts['a'])
        b.update(counts['b'])
        c.update(counts['c'])
        d.update(counts['d'])
        plus.update(counts['+'])
        samurai.display_samurai(ans)
    else:
        print("Puzzle Unsolvable!")



    # Write grid counts to csv files
    write_counter_to_database('grid_a_success_hits.csv', a)
    write_counter_to_database('grid_b_success_hits.csv', b)
    write_counter_to_database('grid_c_success_hits.csv', c)
    write_counter_to_database('grid_d_success_hits.csv', d)
    write_counter_to_database('grid_plus_success_hits.csv', plus)

    print('#'*100)
    print("Successes:     ", success_counter)
    print('#'*100)

