def read_input():
  with open(r"solutions/inputs/day_5.txt", "r") as txt:
    input_list = txt.read().split("\n")
    return input_list

def problem_1():
  readings = read_input()
  all_coordinates = {}
  for reading in readings:
    r1,r2 = map(str.strip, reading.split("->"))
    x1,y1 = map(int, r1.split(","))
    x2,y2 = map(int,r2.split(","))    

    if x1 == x2:
      # horizontal line

      for y in range(min([y1,y2]), max([y1,y2])+1):
        current_coordinate = str(x1) + "," + str(y)
        if current_coordinate in all_coordinates:
          all_coordinates[current_coordinate] += 1
        else:
          all_coordinates[current_coordinate] = 1

    if y1 == y2:
      # vertical line
      for x in range(min([x1,x2]), max([x1,x2])+1):
        current_coordinate = str(x) + "," + str(y1)
        if current_coordinate in all_coordinates:
          all_coordinates[current_coordinate] += 1
        else:
          all_coordinates[current_coordinate] = 1

  print(len([i for i in all_coordinates.values() if i > 1]))


def problem_2():
  pass