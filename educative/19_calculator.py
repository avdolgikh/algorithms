# https://www.educative.io/module/page/8q5JgjuzjGkprAwQG/10370001/6521069168754688/4922943739789312


def calculator(s: str) -> int:
    stack = []  # Stack to store (current_result, current_sign)
    current_result = 0
    current_sign = 1  # 1 for '+', -1 for '-'
    digits = ""

    for c in s:
        if c.isdigit():
            digits += c
        else:
            if digits:
                current_result += current_sign * int(digits)
                digits = ""

            if c == '+':
                current_sign = 1
            elif c == '-':
                current_sign = -1
            elif c == '(':
                stack.append((current_result, current_sign))
                current_result, current_sign = 0, 1
            elif c == ')':
                if digits:
                    current_result += current_sign * int(digits)
                    digits = ""
                last_result, last_sign = stack.pop()
                current_result = last_result + last_sign * current_result

    if digits:
        current_result += current_sign * int(digits)

    return current_result


if __name__ == "__main__":
    for s in [
        "(46 - 12) + (13 - 8)",
        "(13 + 50) + (56 - 29 - (7 + 2))",
        "12 - (6 + 2) + 5",
    ]:
        print(f"{s} --> {calculator(s)}")
