# https://www.educative.io/module/page/8q5JgjuzjGkprAwQG/10370001/4896118288416768/6046584963596288


def is_bad_version(v):
    return bad_version <= v


def first_bad_version(n):
    i, j = 1, n
    api_call_count = 0
    while i <= j:
        m = int((i + j)/2)
        if is_bad_version(m):
            bad_version = m
            j = m - 1
        else:
            i = m + 1
        api_call_count += 1

    return [bad_version, api_call_count]


if __name__ == "__main__":
    for n in range(1, 8):
        for bad_version in range(1, n):
            calc_bad_version, api_calls = first_bad_version(n)
            print(f"{calc_bad_version == bad_version}, api_calls={api_calls}")
