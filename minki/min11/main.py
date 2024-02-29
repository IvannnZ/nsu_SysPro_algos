def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    count_nums = [0, 0, 0]
    point_start = 0
    point_iter = 0
    point_end = len(nums) - 1

    def iter_rom_start():
        if nums[point_start] == 1:
            count_nums[1] += 1
        elif nums[point_start] == 0:
            iter_from_end()
        nums[point_start] = 0
        point_start += 1
        point_iter = max(point_iter, point_start)

    def iter_from_end():
        if nums[point_end] == 1:
            count_nums[1] += 1
        elif nums[point_end] == 0:
            iter_from_start()
        nums[point_end] = 2
        point_end += 1
        point_iter = max(point_iter, point_end)

    while point_end - point_start != count_nums[1]:
        if nums[point_iter] == 0:
            point_start += 1
        elif nums[point_iter] == 1:
            count_nums[1] += 1
        elif nums[point_iter] == 2:
            iter_from_end()
        point_iter += 1
    while point_start != point_end:
        nums


arr = [2, 0, 2, 1, 1, 0]
print(arr[0])
sortColors(arr)

print(arr)
