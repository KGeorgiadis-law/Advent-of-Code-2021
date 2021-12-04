def create_char_list(ls):
  # create lists with the characters of each number in 
  # input list
  return_list = []
  for char in range(len(ls[0])):
    temp_list = [i[char] for i in ls]
    return_list.append(temp_list)
  return return_list

def read_input():
  with open(r"solutions/inputs/day_3.txt", "r") as txt:
    input_list = txt.read().split("\n")
    return input_list

def problem_1():
  input_list = create_char_list(read_input())
  gamma = ""
  epsilon = ""
  for char_list in input_list:
    gamma += "0" if char_list.count('0') > char_list.count('1') else "1"
    epsilon += "0" if char_list.count('1') > char_list.count('0') else "1" 
  print(gamma, epsilon,int(gamma, 2) * int(epsilon, 2))


def recurse(ls, tp="most", i = 0):
  
  char_list = [c[i] for c in ls]

  ones = char_list.count('1')
  zeroes = char_list.count('0') 

  if tp=="most":
    filtr = '1' if ones > zeroes or ones == zeroes else '0'
  else:
    filtr = '0' if ones > zeroes or ones == zeroes else '1'
  
  new_ls = [x for x in ls if x[i] == filtr]
  
  
  if len(new_ls) != 1:
    return recurse(new_ls, tp, i=i+1)
  else:
    return new_ls[0]
    
def problem_2():
  input_list = read_input()
  o2_rating = recurse(input_list, "most")
  Co2_rating = recurse(input_list, "least")

  print(o2_rating, Co2_rating, 
    int(o2_rating,2)*int(Co2_rating,2))