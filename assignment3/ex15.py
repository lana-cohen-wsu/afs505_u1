from sys import argv

# gets 2 arguments, script and text file
script, filename = argv

txt = open(filename)

print(f"File {filename}:")
print(txt.read())

print("Type filename again:")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())

#close files and variables
close(filename)
close(file_again)
close(txt)
close(txt_again)
