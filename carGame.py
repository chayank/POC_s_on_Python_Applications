msg1="start- to start the car"
msg2="stop - to stop the car"
msg3="quit - to exit"
msg4="I don't undertsand"
msg5="Car started ... ready to go!! "
msg6="Car stopped "
msg7="Quitting the game"

while 1==1:
    cmd = input().lower()
    if(cmd =="help"):
        print(msg1+"\n"+msg2+"\n"+msg3)
    elif(cmd == "start"):
        print(msg5)
    elif(cmd=="stop"):
        print(msg6)
    elif(cmd=="quit"):
        print(msg7)
        break
    else:
        print("I don't undertsand")