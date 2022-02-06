"""An oracle that predicts the future."""

from random import randint

input("Ask a yes/no question: ")

response: int = randint(0, 3)
print(response)

if response ==0:
    print("most definately")
else:
    if response == 1:
        print("highly likely")
    else: 
        if response == 2:
            print("ask again later")
        else:
            print()