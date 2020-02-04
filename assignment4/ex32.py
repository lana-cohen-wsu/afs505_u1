count = [4,5,6,7,8]
dogs = ['Saskia','Percy','Cushman']
money = [1,'pennies',10,'dimes',25,'quarters']

for number in count:
    print(f"this is count {number}")

for dog in dogs:
    print(f"this is a dog: {dog}")

for i in money:
    print(f"I got {i}")

elements = []

for i in range(0,6):
    print(f"Adding {i} to the list.")
    elements.append(i)

for i in elements:
    print(f"Element was: {i}")
