# https://www.deep-ml.com/problem/Matrix%20times%20Vector


import numpy as np


def matrix_dot_vector(a : list[list[int|float]], b : list[int|float]) -> list[int|float]:
	c = []
	for a_row in a:
		if len(a_row) != len(b):
			return -1
		c_value = 0
		for a_value, b_value in zip(a_row, b):
			c_value += a_value * b_value
		c.append(c_value)
	return c


if __name__ == "__main__":
	for matrix, vector in [
		# (
		# 	[[1, 3], [3, 4], [4, 5]],
		# 	[1, 2, 3],
        # ),
		(
			[[1, 3], [3, 4], [4, 5]],
			[1, 2],
        ),
    ]:
		print(f"{matrix_dot_vector(matrix, vector)} and True is {np.array(matrix) @ np.array(vector)}")
