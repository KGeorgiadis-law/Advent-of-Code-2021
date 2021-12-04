def read_input():
  with open(r"solutions/inputs/day_4.txt", "r") as txt:
    input_list = txt.read().split("\n\n")
    numbers = [int(x) for x in input_list[0].split(",")]
    boards = [x.split("\n") for x in input_list[1:]]
    clean_boards = []

    for board in boards:
      all_lines = []
      for line in board:
        # extract numbers
        # with thanks to https://stackoverflow.com/a/4289557
        all_lines.append([int(s) for s in line.split() if s.isdigit()])
      clean_boards.append(all_lines)

    return numbers,clean_boards

import numpy as np

def problem_1():
  numbers, boards = read_input()

  # convert the boards to a numpy grid for easier searching, replacing
  grid = np.array(boards, dtype="int")

  # start the bingo!
  for number in numbers:
    # with thanks to https://stackoverflow.com/a/19666680
    grid[grid == number] = "0"
    b = np.where(~grid.any(axis=1))[0]
    if len(b) > 0:
      winning_board = grid[b[0]]
      winning_board_sum = np.sum(winning_board.flatten())
      print(winning_board_sum, number, winning_board_sum*number)
      break

def problem_2():
  grid = np.array([[[1,1,0],[1,2,0],[4,5,0]], [[0,0,1],[1,2,0],[4,5,1]]], "int")
  # b = np.where(~grid.any())[0]
  # print(b)

  # to check both rows and columns, create a transposed instance as well
  for board in grid:
    transposed_board = board.transpose()
    a = np.where(~board.any(axis=1))[0]
    b = np.where(~transposed_board.any(axis=1))[0]
    
    if len(a) > 0:
      print("original: ",board)
    
    if len(b) > 0:
      print("transposed: ",transposed_board)


  # b = np.where(~transposed_grid.any())[0]
  # print(b)

  # numbers, boards = read_input()
  
  # # convert the boards to a numpy grid for easier searching, replacing
  # grid = np.array(boards, dtype="int")

  # # start the bingo!
  # for number in numbers:
  #   # with thanks to https://stackoverflow.com/a/19666680
  #   grid[grid == number] = "0"
  #   b = np.where(~grid.any(axis=1))[0]#
  #   if len(b) > 1:
  #     print(grid[b[0]])
  #     print(grid[b[1]])
  #     break
  #     # winning_board = grid[b[0]]
  #     # winning_board_sum = np.sum(winning_board.flatten())
  #     # print(winning_board_sum, number, winning_board_sum*number)
  #     # break

  