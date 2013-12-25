from cspbase import *
from sudoku_csp import *
import time

##Easy
board0 = [[0,0,2,0,9,0,0,6,0],
          [0,4,0,0,0,1,0,0,8],
          [0,7,0,4,2,0,0,0,3],
          [5,0,0,0,0,0,3,0,0],
          [0,0,1,0,6,0,5,0,0],
          [0,0,3,0,0,0,0,0,6],
          [1,0,0,0,5,7,0,4,0],
          [6,0,0,9,0,0,0,2,0],
          [0,2,0,0,8,0,1,0,0]]


##Easy
board1 = [[1,0,6,0,8,0,3,0,0],
          [0,9,7,4,0,1,0,0,0],
          [0,5,0,3,0,0,7,0,0],
          [4,0,0,0,0,7,0,6,0],
          [2,0,0,0,0,0,0,0,8],
          [0,7,0,5,0,0,0,0,9],
          [0,0,3,0,0,9,0,1,0],
          [0,0,0,2,0,3,8,5,0],
          [0,0,8,0,6,0,9,0,4]]

##Hard
board2 = [[0,7,0,8,5,0,0,0,0],
          [0,9,0,0,0,1,5,0,6],
          [0,0,0,3,0,0,4,0,0],
          [0,3,0,0,0,0,0,0,8],
          [1,0,5,0,0,0,7,0,3],
          [7,0,0,0,0,0,0,2,0],
          [0,0,1,0,0,6,0,0,0],
          [2,0,3,7,0,0,0,6,0],
          [0,0,0,0,3,2,0,1,0]]

##Hard
board3 = [[0,0,9,0,0,2,0,0,0],
          [0,3,0,0,9,0,0,0,0],
          [0,5,0,7,8,0,0,0,9],
          [0,4,0,3,0,0,2,0,0],
          [0,0,7,2,0,8,5,0,0],
          [0,0,1,0,0,5,0,6,0],
          [6,0,0,0,7,9,0,8,0],
          [0,0,0,0,2,0,0,5,0],
          [0,0,0,4,0,0,7,0,0]]

##Easy
boardX = [[3,1,2,5,9,0,7,6,0],
          [9,4,6,7,3,1,2,5,8],
          [8,7,0,4,2,6,9,1,3],
          [5,6,0,0,0,0,3,0,0],
          [0,8,1,0,6,0,5,0,0],
          [2,9,3,1,7,5,4,0,6],
          [1,3,0,0,5,7,0,4,0],
          [6,5,0,9,1,3,8,2,0],
          [0,2,0,0,8,0,1,0,0]]


print '--------------------- Test: Model # 1 ---------------------\n'

t = int(round(time.time() * 1000))
sudoku_enforce_gac_model_1(board0)
print 'Time: ' + str(int(round(time.time() * 1000)) - t) + '\n'

t = int(round(time.time() * 1000))
sudoku_enforce_gac_model_1(board1)
print 'Time: ' + str(int(round(time.time() * 1000)) - t) + '\n'

t = int(round(time.time() * 1000))
sudoku_enforce_gac_model_1(board2)
print 'Time: ' + str(int(round(time.time() * 1000)) - t) + '\n'

t = int(round(time.time() * 1000))
sudoku_enforce_gac_model_1(board3)
print 'Time: ' + str(int(round(time.time() * 1000)) - t) + '\n'

###################################

print '--------------------- Test: Model # 2 ---------------------\n'

t = int(round(time.time() * 1000))
sudoku_enforce_gac_model_2(board0)
print 'Time: ' + str(int(round(time.time() * 1000)) - t) + '\n'

t = int(round(time.time() * 1000))
sudoku_enforce_gac_model_2(board1)
print 'Time: ' + str(int(round(time.time() * 1000)) - t) + '\n'

t = int(round(time.time() * 1000))
sudoku_enforce_gac_model_2(board2)
print 'Time: ' + str(int(round(time.time() * 1000)) - t) + '\n'

t = int(round(time.time() * 1000))
sudoku_enforce_gac_model_2(board3)
print 'Time: ' + str(int(round(time.time() * 1000)) - t) + '\n'

###################################

print '--------------------- Test: Model # 3 ---------------------\n'

t = int(round(time.time() * 1000))
sudoku_enforce_gac_model_3(board0)
print 'Time: ' + str(int(round(time.time() * 1000)) - t) + '\n'

t = int(round(time.time() * 1000))
sudoku_enforce_gac_model_3(board1)
print 'Time: ' + str(int(round(time.time() * 1000)) - t) + '\n'

t = int(round(time.time() * 1000))
sudoku_enforce_gac_model_3(board2)
print 'Time: ' + str(int(round(time.time() * 1000)) - t) + '\n'

t = int(round(time.time() * 1000))
sudoku_enforce_gac_model_3(board3)
print 'Time: ' + str(int(round(time.time() * 1000)) - t) + '\n'

    
