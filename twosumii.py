from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
      nlen: int = len(numbers)
      print("nlen", nlen, list(range(0,nlen)))
      i1_range = range(0, nlen-1)
      print(f"i1 range {list(i1_range)}")
      for i1 in i1_range:
        i2_range = range(nlen-1, i1_range.start, -1)
        print(f"i1[{i1}] i2{list(i2_range)}")
        for i2 in i2_range:
          print(f"n[{i1}] n[{i2}]")
          print(f"{numbers[i1]} + {numbers[i2]} == {target}")
          if numbers[i1] + numbers[i2] == target:
            return [i1+1, i2+1]
      return []
        
      #for i2 in range(len(numbers)-1):
      
        
      
