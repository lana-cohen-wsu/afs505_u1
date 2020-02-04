print("input choice (1 or 2):")
door = input(">")

if  door =="1":
  print("next choice, A or B:")
  bear = input(">")

  if bear =="A":
    print("you picked A")
  elif bear =="B":
    print("you picked B")
  else:
    print(f"you picked {bear} instead")

elif door =="2":
  print("next choice, X or Y")
  mouse = input(">")

  if mouse =="X" or mouse =="Y":
    print("you picked X or Y")
  else:
    print(f"you didn't pick X or Y, but: {mouse}")

else:
  print(f"you didn't choose 1 or 2")
