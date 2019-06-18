# Problem:
# Read the amount of money you have and the prices of the items you intend to buy. Determine
# whether you have enough money to buy everything you selected or whether you are short of
# money. If you do not have enough money, indicate the amount of the shortfall. Be sure to
# include 8% tax when figuring the amount you need.


num = input("Enter array of numbers: ")
numArr = num.split(' ')

# determine the amount you have and the amount you owe
first = True
owed = 0

for i in numArr:
    if first:
        owned = float(i)
        first = False
        continue
    elif i == "-1":
        break

    owed += float(i)

owed += owed * .08  # add tax

if owned > owed:
    print("ENOUGH MONEY")
else:
    print("$" + str(float(owed) - float(owned)) + " SHORT")

exit(0)
