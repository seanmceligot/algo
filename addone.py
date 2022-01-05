
from collections import deque

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # set carry to 0
        # start from size-1 (least significant)
        #add one + carry
        #  if sum >9
        #    set plusone_array[index] = 0
        #     set carry to sum - 9
        #  continue to copy until index = 0
        # return plusone_array 
        
        # deque
        #q.addleft(3)
        #q.addleft(2)
        #q.addleft(1)
        #list(q)
        #print(deque.insert.__doc__) 
        #test = deque()
        #test.insert(0, 2)
        #test.insert(0, 1)
        #assert list(test) == [1,2]
        carry = 0 
        plusone = deque()
        index = len(digits)-1
        done = False
        add = 1
        while index >= 0:
          #ex [0][9]
          n = digits[index] # 9
          isum = n + carry + add # 9 + 0 + 1 = 10
          add = 0
          #print(f"n {n} c {carry} s {isum}")
          carry = 0
          if isum > 9:
            carry, isum = 1, isum-10 #     ## -> 1, 0
            #print(f"c {carry}, s {isum}")
          plusone.insert(0,isum)
          index-=1
          #print(f"i {index} c {carry}")
        if carry:
          plusone.insert(0, carry)
        return list(plusone)
          
