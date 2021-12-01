def problem_1():
  with open("day_1.txt", "r") as puzzle_input_txt:
    puzzle_input = puzzle_input_txt.read().split("\n")
    
    print(puzzle_input[0], puzzle_input[-1])

    increases = []

    for i, depth in enumerate(puzzle_input):
      try:
        if int(puzzle_input[i]) > int(puzzle_input[i-1]):
          increases.append("TRUE") 
        else:
          increases.append("FALSE")
      except IndexError:
        increases.append("FALSE")
    
    print(len([x for x in increases if x == "TRUE"]))

def problem_2():
  with open("day_1.txt", "r") as puzzle_input_txt:
    puzzle_input = puzzle_input_txt.read().split("\n")
    
    print(puzzle_input[0], puzzle_input[-1])

    increases = []

    for i, depth in enumerate(puzzle_input):
      try:
        if int(puzzle_input[i]) + int(puzzle_input[i+1]) + int(puzzle_input[i+2]) > int(puzzle_input[i-1]) + int(puzzle_input[i]) + int(puzzle_input[i+1]):
          increases.append("TRUE") 
        else:
          increases.append("FALSE")
      except IndexError:
        increases.append("FALSE")
    
    print(len([x for x in increases if x == "TRUE"]))
  
