"""EX_03: the 6-turn worldle."""

__author__ = "730487849"


def contains_char(secret: str, search_letter: str) -> bool:
    """Searching for a letter."""
    assert len(search_letter) == 1
    index: int = 0
    while index < len(secret):  
        if search_letter == secret[index]:
            return True
        else:
            index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Giving back emojis."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    storage: str = ""
    index: int = 0
    while index < len(guess):
        if not contains_char(secret, guess[index]):
            storage += WHITE_BOX
            index += 1
        elif guess[index] == secret[index]:
            storage += GREEN_BOX
            index += 1
        else:
            storage += YELLOW_BOX
            index += 1
    return storage


def input_guess(expected_len: int) -> str:
    """Gives back the expected length of the word."""
    guess: str = input(f'Enter a {expected_len} character word: ')
    while len(guess) != expected_len:
        guess = input(f"That wasn't {expected_len} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    length: int = len(secret)
    n: int = 1
    correct: bool = False
    while n < 7 and not correct:
        print(f"=== Turn {n}/6 ===")
        guess: str = input_guess(length)
        print(emojified(guess, secret))
        if guess == secret:
            correct = True
        else:
            n += 1
    if correct:
        print(f"you won in {n}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
