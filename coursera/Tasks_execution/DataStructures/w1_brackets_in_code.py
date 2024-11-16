# Uses python3

import numpy as np

# []{}()
test_cases = { "[]": "Success",
               "{}[]": "Success",
               "[()]": "Success",
               "(())": "Success",
               "{[]}()": "Success",
               "{": 1,
               "{[}": 3,
               "foo(bar);": "Success",
               "foo(bar[i); ": 10, }

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def is_balanced(code):
    opening_brackets_stack = []

    for index, char in enumerate(code):
        if char in "([{":
            opening_brackets_stack.append(char)
            opening_brackets_stack.append(index + 1)
        elif char in ")]}":
            if not any(opening_brackets_stack):
                return index + 1
            _ = opening_brackets_stack.pop()
            opening_bracket = opening_brackets_stack.pop()
            if not are_matching(opening_bracket, char):
                return index + 1

    if not any(opening_brackets_stack):
        return "Success"
    else:
        return opening_brackets_stack[1]

if __name__ == '__main__':
    S = input()
    # The length of S is at least 1 and at most 10**5

    print(is_balanced(S))

    #for case in test_cases:
    #    result = is_balanced(case)        
    #    if result != test_cases[case]:
    #        print("case: {}, test_cases[case]: {}, result: {}".format(case, test_cases[case], result))



