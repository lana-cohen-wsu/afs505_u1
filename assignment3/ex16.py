from sys import argv

script, filename = argv

print(f"ERASE {filename}")
print("if you don't want to, hit CTRL+C")
print("if you do want that, hit RETURN")

input("?")

print("OPENING...")
target = open(filename, 'w')

print("TRUNCATING the file.")
target.truncate()

print("please give 3 lines")

line1 = input("1:")
line2 = input("2:")
line3 = input("3:")

print("these will be written to file")

stuff = str(line1,"\n",line2, "\n", line3,"\n")
target.write(stuff)
#target.write(line3)

print("close file")
target.close()
