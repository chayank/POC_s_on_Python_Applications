guess_count=1
while guess_count<=5:
    print('*' * guess_count)
    guess_count= guess_count + 1
print("done")

secret_number=9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=input("Guess")
    guess_count+=1
    if(int(guess)==secret_number):
        print("right answer")
        break
    else:
        print("wrong answer")
else:
    print("sorry you failed")
