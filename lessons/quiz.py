print(remove_ws("    ok bidcuabfuha  ok"))


def remove_ws(word: str) -> str:
    """Removes whitespace around word."""
    new_word: str = ""
    i: int = 0
    while i < len(word):
        if(word[i] != " "):
            new_word += word[i]
        i += 1
    return new_word


if __name__ == "__main__":
    main()