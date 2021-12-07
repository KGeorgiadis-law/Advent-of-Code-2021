def read_input():
  with open(r"solutions/inputs/day_6.txt", "r") as txt:
    input_list = list(map(int, txt.read().split(",")))
    return input_list

def problem_1():
  fish_population = read_input()
  
  for i in range(80):
    new_fish_today = []
    for f,fish in enumerate(fish_population):
      if fish == 0:
        fish_population[f] = 6
        new_fish_today.append(8)
      else:
        fish_population[f] -= 1
    fish_population = fish_population + new_fish_today

  print(len(fish_population))

import numpy as np

def problem_2_abandoned():
  ## ABANDONED BECAUSE WAS TAKING UP TOO MUCH MEMORY, COULD NOT COMPUTE
  fish_population = np.array(read_input())

  def helper_fun(fish_population):
    new_fish = fish_population[fish_population == 0].size
    fish_population[fish_population == 0] = 7
    fish_population[fish_population != 0] -= 1
    added_fish_population = np.append(fish_population, [8]*new_fish)
    return added_fish_population
  
  for i in range(256):
    fish_population = helper_fun(fish_population)

  print(fish_population.size)

def problem_2():
  fish_population = read_input()
  fish_population_dict = {}
  for i in range(9):
    fish_population_dict[i] = 0
  
  for fish in fish_population:
    fish_population_dict[fish] += 1

  for i in range(256):
    new_fish = fish_population_dict[0]
    # print(new_fish)
    for age in fish_population_dict.keys():
      if age != 0:
        fish_population_dict[age-1] = fish_population_dict[age]
    fish_population_dict[8] = new_fish
    fish_population_dict[6] += new_fish
  print(sum(fish_population_dict.values()))