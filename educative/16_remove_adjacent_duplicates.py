# https://www.educative.io/module/page/8q5JgjuzjGkprAwQG/10370001/6521069168754688/6392718995226624

from collections import deque


def remove_duplicates(s):
    stack = deque()
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return ''.join(list(stack))


if __name__ == "__main__":
    for s in [
        "azxxzy",
        "azxxzzy",
    ]:
        print(f"{s}  ===>  {remove_duplicates(s)}")


