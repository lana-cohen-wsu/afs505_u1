from sys import argv
script, start, finish, incr = argv

def main(start, finish, incr):
  i = float(start)
  finish = float(finish)
  incr = float(incr)
  numbers = []  
  while i < finish:
    #print(f"At the top i is {i}")
    numbers.append(i)
    i += incr
    #print("Numbers now:", numbers)
  #print(f"At the bottom i is {i}")
  #print("The numbers:")
  for num in numbers:
    print(num)

main(start,finish,incr)
