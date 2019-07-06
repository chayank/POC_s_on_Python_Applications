num=(1,2,3)

#contains the below functions

num.count(3)
num.index(1)

# cannot change it, they are immutable
# similar to lists


#unpacking - most importamnt feature in python

coordinates=(1,2,3)
x,y,z=coordinates
print(y)



#Dictionaries

cust={
    "name":"john smith",
    "age":30,
    "is_verified":True
}

print(cust.get("name"),"yolo")

print(cust["name"])


# enter: 1234 ,result : one two three four
number={
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five"
}
msg=""
num=input("enter a number which contains digits between 1 and 5")
for item in num:
    msg=msg+number.get(int(item),"!")+" "
print(msg)

