# https://www.educative.io/module/page/8q5JgjuzjGkprAwQG/10370001/6521069168754688/5404322332147712


def find_exit_column(grid):
    m = len(grid)
    n = len(grid[0])
    cache = {}
    result = []

    for ball in range(n):
        col = ball
        ball_path = []
        for row in range(m):
            # check cached result
            if (row, col) in cache:
                col = cache[(row, col)]
                break
            ball_path.append((row, col))

            direction = grid[row][col]
            # check walls and V-shape 
            if (
                (direction == -1 and col == 0)  # left wall
                or (direction == 1 and col == n-1)  # right wall 
                or (grid[row][col + direction] == -1 * direction)  # V-shape
            ):
                col = -1
                break

            # move to the next level
            col += direction

        # save the ball final column
        result.append(col)

        # fill the cache
        for cell in ball_path:
            cache[cell] = col

    return result


if __name__ == "__main__":
    for grid in [
        [[1, 1], [-1, -1]],
        [[-1, 1], [-1, -1]],
        [[-1, -1], [1, 1]],
        [[1, 1, 1, -1], [-1, -1, 1, 1], [1, 1, -1, -1], [-1, -1, 1, 1]],
    ]:
        print(f"{grid} --> {find_exit_column(grid)}")
