#Tip Calculator (day 2)

print("Welcome to the tip calculator.")
print("What was the total bill?")
bill_amount = input()
print("What percentage of tip would you like to give?")
tip_percentage= input()
print("How many people to split the bill?")
people=input()

#New amount with the tip included
amount_new= int(bill_amount) + (int(bill_amount)*int(tip_percentage)/100)

#Amount is getting splitted into people
amount_split= amount_new/int(people)
print("Each person has to pay " + str(amount_split))
