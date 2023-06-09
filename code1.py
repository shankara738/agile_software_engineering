grid = [
  [5,7,8,3,4,6,1,2,9],
  [1,2,3,4,5,6,7,8,9],
  [9,8,7,6,5,4,3,2,1],
  [1,3,5,7,9,2,4,6,8],
  [2,4,6,8,1,9,3,5,7],
  [1,2,4,5,7,8,3,6,9],
  [9,8,6,5,3,2,1,4,7],
  [2,5,8,6,3,1,7,9,4],
  [9,1,3,2,5,4,6,8,7]
]
row_no = 2
element = 8
def check_row(grid, row_no, element):
  for col in range(9):
    if(grid[row_no][col] == element):
      return True
    print("False")

print(check_row(grid,row_no,element))

column_no = 3
element = 5
def check_column(grid, column_no, element):
  for col in range(9):
    if(grid[column_no][col] == element):
      return True
    print("False")

print(check_row(grid,3,5))

def print_diagonal(grid):
  for i in range(9):
    print(grid [i] [i])

print_diagonal(grid)
