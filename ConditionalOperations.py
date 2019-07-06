is_hot=False
is_cold=True
if is_hot:
    print("its a hot day")
    print("drink a plenty of water")
elif is_cold:
    print("its a cold day")
    print("wear  warm clothes")
else:
    print("it's a lovely day")


#price of house is 1M
#if buyer has good credit
#they need to put down  105
#otherwise#they need to put down 20%

price_house=100000
has_goodcredit= True
print("price of the house  : "+str(price_house))
if has_goodcredit:
    print("buyer needs to pay 10% : "+str(0.1*price_house))
else:
    print("buyer needs to pay 20% :"+str(0.2*price_house))

#logicval operators

if has_goodcredit and is_hot :
    print("he is a stud... lol")

if has_goodcredit or is_hot :
    print("he is a stud... lol")

if has_goodcredit and not is_hot :
    print("he is a stud... lol")


#comparison operators

temperature = 35
if temperature>38:
    print("its a hot day")
if temperature<38:
    print("its a crazy day")


#excercise


weight=input("enter your weight : ")
lbs_or_kgs=input("(L)bs or (K)gs :")
if lbs_or_kgs.upper()=="K":
    print('You are '+str(float(weight)*2.20)+' pounds')
elif lbs_or_kgs.upper()=="L":
    print('You are '+str(float(weight) / 2.20)+' kgs')
else:
    print("invalid entry")

# // gives a integer