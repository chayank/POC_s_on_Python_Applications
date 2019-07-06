first= "john"
last="doe"

message=first + " ["+last+"] is name"
# this becomes diffcult to reads for programmers

#so we use formatters

msg=f'{first} [{last}] is name used with formatters'

print(message)

print(msg)
