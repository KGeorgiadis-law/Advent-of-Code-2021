# relatively happy with this!

def read_input():
  with open(r"solutions/inputs/day_2.txt", "r") as txt:
    input_list = txt.read().split("\n")
    return input_list

def problem_1():
  directions = read_input()
  horizontal = 0
  vertical = 0

  horizontal_axes = {
    "forward": 1,
  }

  vertical_axes = {
    "up": -1,
    "down": 1,
  }

  for line in directions:
    direction, value = line.split()
    if direction in horizontal_axes:
      horizontal += int(value) * horizontal_axes[direction]
    
    elif direction in vertical_axes:
      vertical += int(value) * vertical_axes[direction]

  print(horizontal,vertical,horizontal * vertical)

def problem_2():
  directions = read_input()
  horizontal = 0
  vertical = 0
  aim = 0

  horizontal_axes = {
    "forward": 1,
  }

  vertical_axes = {
    "up": -1,
    "down": 1,
  }

  for line in directions:
    direction, value = line.split()
    if direction in horizontal_axes:
      horizontal += int(value) * horizontal_axes[direction]
      vertical += int(value) * aim
    
    elif direction in vertical_axes:
      aim += int(value) * vertical_axes[direction]

  print(horizontal,vertical,horizontal * vertical)