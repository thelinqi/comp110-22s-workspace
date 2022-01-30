"""EX02 - One Shot Wordle."""

__author__ = "730487849"

# start the prompt!
secret: str = "python"
guess = str(input("What is your " + str(len(secret)) + "-letter guess? "))

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# wrong number of letters for input
while int(len(guess)) != len(secret):
    guess = input("That was not " + str(len(secret)) + " letters! Try again: ")

# checking indices for correct matches
index: int = 0
storage: str = ""

while index < len(secret):
    if guess[index] == secret[index]:
        storage += GREEN_BOX
    # checking correct letters at incorrect positions
    else:
        anywhere: bool = False
        another_index: int = 0
        while not anywhere and another_index < len(secret):
            if guess[index] == secret[another_index]:
                anywhere = True
            else:
                another_index = another_index + 1
        if anywhere:
            storage += YELLOW_BOX
        else:
            storage += WHITE_BOX
    index = index + 1
print(storage)

# final stage!
if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")