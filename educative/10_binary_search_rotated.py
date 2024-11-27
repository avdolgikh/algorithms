# https://www.educative.io/module/page/8q5JgjuzjGkprAwQG/10370001/4896118288416768/6562044456992768

def binary_search_rotated(nums, target):
    low, high = 0, len(nums)-1
    while low <= high:
        mid = int((low + high)/2)
        # print(f"low={low}, high={high}, mid={mid}")
        if target == nums[mid]:
            return mid
        elif nums[low] <= nums[mid]:  # the left is sorted 
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:  # the right is sorted 
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


if __name__ == "__main__":
    for nums, target, true_index in [
        ([6, 7, 1, 2, 3, 4, 5], 2, 3),
        ([176, 188, 199, 200, 1, 2, 3], 199, 2),
        ([1, 2, 3, 4, 5, 6, 7], 8, -1),
        ([9, 10, 1, 2, 3, 4, 5, 6, 7], 8, -1),
        ([2, 3, 4, 5, 6, 7, 1], 1, 6),
        ([3, 4, 5, 6, 7, 1, 2], 2, 6),
        ([7, 8, 2, 3, 4, 5, 6], 7, 0),
        ([6, 7, 1, 2, 3, 4, 5], 1, 2),
        ([6, 7, 8, 1, 2, 3, 4, 5], 1, 3),
        ([4, 5, 6, 7, 1, 2, 3], 1, 4),
        ([4, 5, 6, 7, 8, 1, 2, 3], 1, 5),
        ([5, 6, 7, 1, 2, 3, 4], 1, 3),
        ([6, 7, 8, 1, 2, 3, 4, 5], 1, 3),
        ([5, 6, 7, 8, 1, 2, 3, 4], 1, 4),
        ([5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4], 1, 8),
        ([5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4], 1, 9),
        ([2, 1], 1, 1),
    ]:
        actual_index = binary_search_rotated(nums, target)
        assert binary_search_rotated(nums, target) == true_index, f"{nums}, target={target}, actual_index={actual_index}, true_index={true_index}"
