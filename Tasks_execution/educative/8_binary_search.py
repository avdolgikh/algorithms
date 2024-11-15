# https://www.educative.io/module/page/8q5JgjuzjGkprAwQG/10370001/4896118288416768/5789606509019136


def binary_search(nums, target):
    i, j = 0, len(nums)-1
    while i <= j:
        m = int((i + j)/2)
        # print(f"i={i}, j={j}, m={m}")
        if target == nums[m]:
            return m
        elif target < nums[m]:
            j = m - 1
        else:
            i = m + 1
    return -1


if __name__ == "__main__":
    for nums, target in [
        ([-5, 10, 19, 35, 210], 40),
        ([-5, 10, 19, 35, 210], -5),
        ([-5, 10, 19, 35, 210], 10),
        ([-5, 10, 19, 35, 210], 19),
        ([-5, 10, 19, 35, 210], 35),
        ([-5, 10, 19, 35, 210], 210),

        ([-5, 10, 35, 210], 40),
        ([-5, 10, 35, 210], -5),
        ([-5, 10, 35, 210], 10),
        ([-5, 10, 35, 210], 35),
        ([-5, 10, 35, 210], 210),
    ]:
        print(binary_search(nums, target))
