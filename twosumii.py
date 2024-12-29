from typing import List

o_count = 0
o_n = 0
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
      global o_count, o_n
      o_count = 0
      nlen: int = len(numbers)
      o_n = nlen
      low: int = 0
      high: int = nlen-1
      print(f"nlen {nlen} numbers {numbers}", nlen, numbers)
      while low < high:
          o_count+=1
          sum = numbers[low] + numbers[high] 
          print(f"low {low} high {high} sum {sum}")
          if sum == target:
            return [low+1, high+1]
          elif sum < target:
              low+=1
          elif sum > target:
              high-=1
      return []

solution = Solution()

if __name__ == "__main__":
    print(solution.twoSum([5,25,75], 100))
    print(f"o_n {o_n} o_count {o_count} {o_count/o_n}")
        
      
