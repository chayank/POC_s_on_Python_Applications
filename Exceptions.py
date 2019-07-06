# exit code 0 means its a success
# anything else is a error


# in python we use try except

try:
    age=int(input('Age: '))
    print(age)
except ZeroDivisionError:
    print("1/0 ")
except ValueError:
    print('Invalid value')


#comments

