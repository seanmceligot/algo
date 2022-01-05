from typing import List, Union
import math


def sum(nums: List[int]):
    count = 0
    for n in nums:
        count += n
    #print(f"sum {nums} = {count}")
    return count


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = current_subarray = nums[0]

        checked = [max_subarray]
        for num in nums[1:]:
            checked += [num]
            #print(f"{checked}\tc=max n:{num} n:{num}+c:{current_subarray}=n:{num+current_subarray}")

            tmpmax = max(num, current_subarray+num)
            #print(f"{checked}\tc=max n:{num} n:{num}+{current_subarray} = {tmpmax}")
            current_subarray = tmpmax

            tmpmmax = max(max_subarray, current_subarray)
            print(
                f"{checked}\tm=max c:{current_subarray}\tm:{max_subarray} = {tmpmmax}")
            max_subarray = tmpmmax
        return max_subarray


sol = Solution()


def check(nums: List[int], ans):
    actual = sol.maxSubArray(nums)
    print(f"maxSubArray({nums}) == {actual}")
    assert actual == ans


check([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)
# maxsum=-2
# -2 + 1 = -1, i = 0, isum-1
# [-2 + 1]=-1 -3 isum=
##        [-2 + 1 -3] +4
##        -2 + 1 -3 +4 -1
##        -2 + 1 -3 +4 -1 +2
##        -2 + 1 -3 +4 -1 +2 + 1
##        -2 + 1 -3 +4 -1 +2 + 1 - 5
# -2 + 1 -3 +4 -1 +2 + 1 - 5 + 4 i=0, i2=size-1
# 1 i=1
##        1 -3
##        1 -3 +4
##        1 -3 +4 -1
##        1 -3 +4 -1 +2
##        1 -3 +4 -1 +2 + 1
##        1 -3 +4 -1 +2 + 1 - 5
##        1 -3 +4 -1 +2 + 1 - 5 + 4
##
##
