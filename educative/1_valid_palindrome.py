# https://www.educative.io/module/page/8q5JgjuzjGkprAwQG/10370001/4896118288416768/5996673417084928

def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    for word in [
        # None,
        "", # clarify the task conditions
        "a", # clarify the task conditions
        "asa",
        "assa",
        "asdfdsa",
        "asdffdsa",
        "asdffdsea",
        "dkfld",
        "ggg",
    ]:
        print(f"{word} -> {is_palindrome(word)}")