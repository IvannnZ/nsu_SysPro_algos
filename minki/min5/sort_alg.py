def arr_step_by_len(len):
    n = 2
    while len > 2 ** n - 1:
        n += 1
    while n > 0:
        n-=1
        yield 2 ** n - 1


def swap(arr: list[int], pos1: int, pos2: int):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]
    return arr


def sort_by_n(arr: list[int], step: int, start: int) -> list[int]:
    for i in range(start + step, len(arr), step):
        if arr[i - step] > arr[i]:
            pivot = i
            while pivot >= step and arr[pivot-step] > arr[pivot]:
                arr = swap(arr, pivot, pivot - step)
                pivot -= step
    return arr

def my_sort(arr: list[int]) -> list[int]:
    for i in arr_step_by_len(len(arr)):
        for j in range(i):
            arr = sort_by_n(arr, i, j)
        print("print arr after n-sorted:", i, arr)
    return arr
    pass


my_sort([3,0,6,1,5])

class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations = my_sort(citations)
        for i in range(len(citations)):
            if citations[i] < i:
                return i - 1
