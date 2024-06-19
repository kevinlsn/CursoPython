# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
#Know de type of the variables
print(type(height))
print(type(height))
#Convert to int y float
height_2 = float(height)
weight_2 = int(weight)
#Operation
bmi= weight_2 / height_2 ** 2
#Print result
print(int(bmi))