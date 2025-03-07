import pyautogui as pg
import numpy as np
import time

sudoku_grid = []

while True:
  row = list(input('Row: '))
  # row = []
  # for i in range(9):
  #   num = int(input(f'Enter number {i+1}: '))
  #   row.append(num)
  ints = []

  for n in row:
    ints.append(int(n))
  sudoku_grid.append(ints)

  if len(sudoku_grid) == 9:
    break
  print("Row " + str(len(sudoku_grid)) + " complete")

time.sleep(3)

# sudoku_grid = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ]

def possible(x,y,n): #position y,x and int n , if n is answer at position y,x
  for i in range(0,9):
    if sudoku_grid[i][x] == n and i != y: #in all rows in cell row,x position nd not in current cell that we are solving i.e. row,x
      return False
    
  for i in range(0,9): #similarly in y row in all cols ,i position and not in current cell that we are solving i.e. y,col
    if sudoku_grid[y][i] == n and i != x:
      return False
    
  x0 = (x // 3) * 3 # take remainder by 3 and multiply by 3 to get either 0,3,6 like the top left cells in each block so if youre in col 0 or col 3 or col 6
  y0 = (y // 3) * 3 # similarl if you are in row 0 , row 3 or row 6
  for X in range(x0 , x0 + 3):
    for Y in range(y0 , y0 + 3):
      if sudoku_grid[Y][X] == n:
        return False

  return True


def Print(matrix):
  # final = []
  str_fin = []
  # for i in range(9):
    # final.append(matrix[i]) ##extrack each row in final

  for lists in matrix: 
    for num in lists: # store each row as string , why?? because when you press keyboard even for numbers it is inputted as strings like '1' , '2' etc.
      str_fin.append(str(num))
  
  print("str_fin is " + str(str_fin))
  counter = []

  for num in str_fin:
    pg.press(num) 
    pg.hotkey('right')
    counter.append(num)
    if len(counter) % 9 == 0:
      pg.hotkey('down')
      for i in range (8):
        pg.hotkey('left')


def solve():
  global sudoku_grid
  for y in range(9):
    for x in range(9):
      if sudoku_grid[y][x] == 0:
        for n in range(1,10):
          if possible(x , y , n):
            sudoku_grid[y][x] = n
            solve()
            sudoku_grid[y][x] = 0
        return
  Print(sudoku_grid) 
  exit() # prevent unnecessary backtracking ;)lkoooo

solve()
# print("hellloooooooo")