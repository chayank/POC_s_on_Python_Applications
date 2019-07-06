bith_year= input('birth year : ')
#age= 2019 -bith_year
#2019 - '1982'
#print(age) - this will result in error as type conversion isn't done.
# in python evrything is converted to string
print(type(bith_year))
age =2019 -int(bith_year)
print(age)

weight_lbs = input('weight (lbs): ')
#weight_kg = weight_lbs * 0.45
# python cannot multiply string with float
weight_kg= int(weight_lbs) * 0.45

# u have to again convert to str to display
print("weight in kg "+ str( weight_kg))