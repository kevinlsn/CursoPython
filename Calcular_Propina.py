print("Welcome to tip calculator")
bill = input("What was the total bill? $")
#Print type
#print(type(bill))
#Convert to float
bill = float(bill)
#Percent of the tip
tip = int(input("How much tip would you like to give? 10, 12, or 15? \n"))
#People on the bill
people = int(input("How many people to split the bill? \n"))
#Calculate the tip
bill_with_tip = tip / 100 * bill + bill
#Print the bill with tip
print(f"Total amount is: ${bill_with_tip}")
#Calcula cuanto es por persona
bill_per_person = bill_with_tip / people
#Cuanto le toca a cada uno
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")