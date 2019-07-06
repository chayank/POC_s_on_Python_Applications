for item in [1,2,3]:
    print(item)

for item in range(5,10):
    print(item)


name= ['abc','asds','sdasd']
print(name[2])


matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0][1])

msg=""
for row in matrix:
    msg=""
    for item in row:
       msg=msg+str(item)
    print(msg)


num=[5,6,7,89]
num.append(20)
num.insert(0,10)
num.insert(0,"ds")

num2=num.copy() # copies all elemnt formt he list

print(num)


que= [2,2,4,4,5,6,7]
print(que)
uni=[]
for number in que:
    if number not in uni:
        uni.append(number)
print(uni)