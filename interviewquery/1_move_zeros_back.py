# https://www.interviewquery.com/questions/move-zeros-back

# Given an array of integers, write a function move_zeros_back that moves all zeros in the array to the end of the array.
# If there are no zeros, return the input array.


# def move_zeros_back(array):
#     left, right = 0, len(array) - 1
#     count = 0
#     while left < right:
#         count += 1
#         if array[left] == 0:
#             array[left], array[right] = array[right], array[left]
#             right -= 1
#         else:
#             left += 1
#     print(f"count: {count}")
#     return array


# def move_zeros_back(array):
#     left, right = len(array) - 2, len(array) - 1
#     count = 0
#     internal_moves = 0
#     while left >= 0:
#         count += 1
#         if array[left] == 0:
#             array[left:right] = array[left+1:right+1]
#             internal_moves += right - left 
#             array[right] = 0
#             right -= 1
#         left -= 1
#         print(f"{array}, internal_moves: {internal_moves}")
#     print(f"count: {count}, internal_moves: {internal_moves}")
#     return array


def move_zeros_back(array):
    non_zero_index = 0

    # Move all non-zero elements to the front of the array
    for i in range(len(array)):
        if array[i] != 0:
            array[non_zero_index] = array[i]
            non_zero_index += 1

    # Fill the rest of the array with zeros
    array[non_zero_index:] = [0]*(len(array)-non_zero_index)

    return array


if __name__ == "__main__":
    for array in [
        [],
        [1], 
        [2, 4, 7],
        [0, 0],
        [0, 4, 0],
        [0, 0, 8, 0, 0],
        [4, 0, 0, 6],
        [0,5,4,2,0,3],
        [0,5,4,2,0,3,0],
        [0, 0, 0, 0, 0, 9],
    ]:
        print(f"{array} --> {move_zeros_back(array)}")
        
    