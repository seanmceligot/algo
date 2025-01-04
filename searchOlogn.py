from typing import List


def search(nums: List[int], target: int, li, ri) -> int:
    searching = nums[li:ri]
    print(f"{li}..{ri} {target} in {searching}")
    mid_index = li + int((ri - li) / 2)
    if ri == li:
        return ri
    assert mid_index >= li
    assert mid_index <= ri
    mid_value = nums[mid_index]
    print(
        f"{li}<{mid_index}>{ri} find {target} in {nums[li:mid_index]} {mid_value} {nums[mid_index+1:ri]}"
    )
    if mid_value == target:
        return mid_index

    print(f"{target} ? {mid_value}")
    if target < mid_value:  ## <- left..mid
        print(f"{target} < {mid_value}")
        print(f"next search le {li} mid_index {mid_index}")
        # if li == mid_index:
        #    return mid_index
        return search(nums, target, li, mid_index)
    else:  ## -> mid..right
        print(f"{target} > {mid_value}")
        print(f"next search le {mid_index+1} ri {ri}")
        return search(nums, target, mid_index + 1, ri)


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return search(nums, target, 0, len(nums))


sol = Solution()


def check(nums, target, expect=None):
    if expect is None:
        expect = target
    ans = sol.searchInsert(nums, target)
    print("got", ans, "expect", expect, "nums[ans]", nums[ans])
    assert ans == expect


for target in range(20):
    check(list(range(20)), target)

# check(list(range(0, 20, 2)), 5)
check(list(range(0, 20, 2)), 17, 9)
