from sys import argv
from os.path import exists

script,from_file,to_file = argv

print(f"copying from {from_file} to {to_file}")

in_data = open(from_file).read()

print(f"input file is {len(in_data)} bytes")
print(f"does output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL+C to abort.")
input()

out_file = open(to_file,'w')
out_file.write(in_data)

print("done")
out_file.close()
