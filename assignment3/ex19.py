def chz_crackers(chz,crackers):
  print(f'you have {chz} cheeses')
  print(f'you have {crackers} boxes of crackers.')

print('can give the numbers directly:')
chz_crackers(20,30)

print('or use variables from the script')
amount_of_cheese = 10
amount_of_crackers = 50
chz_crackers(amount_of_cheese,amount_of_crackers)

print('or do math with variables')
chz_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
