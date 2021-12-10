from typing import List, Union
import math

def sum(nums: List[int]):
    count = 0;
    for n in nums:
      count+= n
    #print(f"sum {nums} = {count}")
    return count

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      maxsum: Union[int,float] = nums[0]
      size = len(nums)
      if size == 0:
        return 0
      for i in range(size):
          isum:int = 0
          for j in range(i, size):
            isum+=nums[j]
            maxsum = max(maxsum, isum)
            #print("max", maxsum)
      if isinstance(maxsum, float):
          return 0
      else:
          return maxsum
# [-2,1,-3,4,-1,2,1,-5,4]
##  maxsum=-2
##        -2 + 1 = -1, i = 0, isum-1
##        [-2 + 1]=-1 -3 isum=
##        [-2 + 1 -3] +4
##        -2 + 1 -3 +4 -1
##        -2 + 1 -3 +4 -1 +2
##        -2 + 1 -3 +4 -1 +2 + 1 
##        -2 + 1 -3 +4 -1 +2 + 1 - 5
##        -2 + 1 -3 +4 -1 +2 + 1 - 5 + 4 i=0, i2=size-1
##        1 i=1
##        1 -3 
##        1 -3 +4
##        1 -3 +4 -1
##        1 -3 +4 -1 +2
##        1 -3 +4 -1 +2 + 1 
##        1 -3 +4 -1 +2 + 1 - 5
##        1 -3 +4 -1 +2 + 1 - 5 + 4
##        
##        

