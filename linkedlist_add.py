from linkedlist import *
from typing import Optional


def add(l1: Optional[ListNode], l2: Optional[ListNode], l3: ListNode):
    next1 = l1
    next2 = l2
    power = 0
    if next1 is not None or next2 is not None:
        v1 = next1.val if next1 is not None else 0
        v2 = next2.val if next2 is not None else 0
        sum = v1*10**power + v2*10**power + l3.val
        #print(f"{v1}*10**{power}+{v2}*10**{power}={sum}")
        carry = 0
        #print(f"{sum} > 10?")
        if sum >= 10:
            sum, carry = (sum % 10),  int(sum/10) 
            #print(f"sum: {sum} carry: {carry}")
        power += 1
        l3.val = sum
        #print(f"l3 {l3.val}")
        next1 = next1.next if next1 else None
        next2 = next2.next if next2 else None
        if next1 or next2 or carry > 0:
            l3.next = ListNode(carry)
            #print(f"l3.next {carry}")
            add(next1, next2, l3.next)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        assert l1 is not None
        assert l2 is not None
        l3 = ListNode()
        add(l1, l2, l3)
        return l3
    def debug_add(self, l1: Optional[ListNode], l2: Optional[ListNode], expected) -> Optional[ListNode]:
        print("l1", linked_list_to_array(l1))
        print("l2", linked_list_to_array(l2))
        result = solution.addTwoNumbers(l1, l2)
        ar_result = linked_list_to_array(result)
        assert ar_result == expected
        print("result", ar_result)

solution = Solution()
if __name__ == "__main__":
    #l1 = linked_list_from_array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
    #l2 = linked_list_from_array([5, 6, 4])
    #solution.debug_add( l1, l2, [6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])

    #l1 = linked_list_from_array([2, 4, 3])
    #l2 = linked_list_from_array([5, 6, 4])
    #solution.debug_add( l1, l2, [7, 0, 8])

    l1 = linked_list_from_array([9,9,9,9,9,9,9])
    l2 = linked_list_from_array([9,9,9,9])
    solution.debug_add( l1, l2, [8,9,9,9,0,0,0,1])
    # n1 = 2*10**0  + 4*10**1 + 3*10**2
    # n2 = 5*10**0  + 6*10**1 + 4*10**2
    # digit1 =2*10**0+ 5*10**0
    # assert digit1 == 7
    # print(n1)
    # print(n2)
    # print(n1+n2)
