# https://www.educative.io/module/page/8q5JgjuzjGkprAwQG/10370001/4896118288416768/6636333810057216

def sort_colors(colors):
    start = 0
    current = 0
    end = len(colors) - 1

    while current <= end:
        if colors[current] == 0:
            colors[current], colors[start] = colors[start], colors[current]
            current += 1
            start += 1
        elif colors[current] == 1:
            current += 1
        else:
            colors[current], colors[end] = colors[end], colors[current]
            end -= 1

    return colors


if __name__ == "__main__":
    colors = [0, 0, 1, 0, 0]  # [0, 1, 0] # [0, 2, 0] # [2, 1, 2] # [0, 1, 0] # [1, 2, 1, 2, 1]  # [2, 1, 1, 0, 2, 2, 1, 0, 0, 1]
    print(colors)
    sort_colors(colors)
    print(colors)

