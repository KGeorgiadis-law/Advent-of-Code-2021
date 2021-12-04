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
      print(winning_board)
      print(winning_board_sum*number)
      break

def problem_2():
  numbers, boards = read_input()
  grid = np.array(boards, dtype="int")

  # convert all 0 to 100. We'll be using 0 to figure out which number is called
  grid[grid == 0] = 100
  
  winning_boards = []

  # start the bingo!
  for number in numbers:

    # all 0 has been converted to 100
    if number == 0:
      number = 100

    grid[grid == number] = 0

    for i,board in enumerate(grid):
      # to check both rows and columns, create a transposed instance as well
      transposed_board = board.transpose()

      # with thanks to https://stackoverflow.com/a/19666680
      a = np.where(~board.any(axis=1))[0]
      b = np.where(~transposed_board.any(axis=1))[0]

      if len(a) > 0 or len(b) > 0:
        # store the winning board along with the number which triggered it
        winning_boards.append((np.copy(board), number))
        grid[i] = -1

  last_winning_board_sum = np.sum(winning_boards[-1][0].flatten()) * winning_boards[-1][1]
  print(winning_boards[-1][0])
  print(last_winning_board_sum)