# https://www.educative.io/module/page/8q5JgjuzjGkprAwQG/10370001/4896118288416768/4879894745710592

def get_next_index(cur_index, shift, length):
    return (cur_index + shift) % length


def circular_array_loop(nums):  
    length = len(nums)

    for num_start_index in range(len(nums)):
        fast_index = get_next_index(num_start_index, nums[num_start_index], length)
        if num_start_index == fast_index:
            continue
        slow_index = num_start_index
        slow = nums[slow_index]
        fast = nums[fast_index]

        while fast_index != slow_index:
            new_fast_index = get_next_index(fast_index, fast, length)
            if new_fast_index == fast_index or nums[new_fast_index] * fast < 0:
               break
            fast_index = new_fast_index
            fast = nums[fast_index]

            new_fast_index = get_next_index(fast_index, fast, length)
            if new_fast_index == fast_index or nums[new_fast_index] * fast < 0:
               break
            fast_index = new_fast_index
            fast = nums[fast_index]

            slow_index = get_next_index(slow_index, slow, length)
            if fast_index == slow_index:
                return True
            
            slow = nums[slow_index]

    return False


if __name__ == "__main__":
    for array in [
        [3, -3, 2, -2],
        [3, 1, 2],
        [-2, -1, -3],
        [2, 1, -1, -2],
    ]:
        print(circular_array_loop(array))
