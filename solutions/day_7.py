def read_input():
  with open(r"solutions/inputs/day_7.txt", "r") as txt:
    input_list = list(map(int, txt.read().split(",")))
    return input_list

import numpy as np

def problem_1():
  crab_positions = np.array(read_input())
  m = np.median(crab_positions)
  diff = np.abs(crab_positions - m)
  print(sum(diff))

def problem_2():
  crab_positions = np.array(read_input())
  m = np.floor(np.mean(crab_positions))

  # numpy solution
  # with thanks to https://study.com/academy/lesson/finding-the-sum-of-consecutive-numbers.html
  # np.abs(crab_positions - m) is the number of steps between current and mean
  processed_crab_positions = (np.abs(crab_positions - m) + 1) / 2 * np.abs(crab_positions - m)
  print(sum(processed_crab_positions))

  # alternative, more readable, for loop approach
  fuel = []
  for crab in crab_positions:
    n = np.abs(crab-m)+1
    crab_fuel = n/2 *(n-1)
    fuel.append(crab_fuel)

  print(sum(fuel))