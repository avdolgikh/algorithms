# https://www.educative.io/module/page/8q5JgjuzjGkprAwQG/10370001/6521069168754688/6664226132983808


def min_remove_parentheses(s: str) -> str:
    op_parentheses_idx = []
    indices_to_remove = set()

    for idx, char in enumerate(s):
        if char == "(":
            op_parentheses_idx.append(idx)
        elif char == ")":
            if op_parentheses_idx:
                # Matched with an opening parenthesis
                op_parentheses_idx.pop()
            else:
                # Unmatched closing parenthesis
                indices_to_remove.add(idx)

    # Add remaining unmatched opening parentheses
    indices_to_remove.update(op_parentheses_idx)

    # Build the resulting string
    return ''.join(char for idx, char in enumerate(s) if idx not in indices_to_remove)


if __name__ == "__main__":
    for s in [
        "a(b",
        "a(b)c)d(",
        "))(((",
        "()()(())"
    ]:
        print(f"{s} --> {min_remove_parentheses(s)}")
