from linkedlist import *

def int_to_linked_list(n: int) -> ListNode:
    head = ListNode()
    cur = head
    import pdb;pdb.set_trace()
    while n > 0:
        cur.val = n%10
        n = int(n/10)
        if n > 0:
            cur.next = ListNode()
            cur = cur.next
    return head
            

def add(l1: ListNode, l2: ListNode) -> int:
   cur1  = l1
   cur2 = l2
   total = 0
   power = 0
   while not (cur1 is None and cur2 is None):
       v1 = cur1.val if cur1 is not None else 0
       v2 = cur2.val if cur2 is not None else 0
       sum = v1*10**power + v2*10**power
       print(f"{v1}*10**{power}+{v2}*10**{power}= {sum}")
       total+=sum
       power+=1
       cur1 = cur1.next if cur1 else None
       cur2 = cur2.next if cur2 else None
   return total 

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        assert l1 is not None
        assert l2 is not None
        total = add(l1, l2)
        print("total", total)
        result:ListNode = int_to_linked_list(total)
        return result


solution = Solution()

if __name__ == "__main__":
    l1 = linked_list_from_array([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
    l2 = linked_list_from_array([5, 6, 4])
    print("l1", linked_list_to_array(l1))
    print("l2", linked_list_to_array(l2))
    result = solution.addTwoNumbers(l1, l2)
    ar_result = linked_list_to_array(result)
    print("result", ar_result)
    assert ar_result == [6,6,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]

    # n1 = 2*10**0  + 4*10**1 + 3*10**2
    # n2 = 5*10**0  + 6*10**1 + 4*10**2
    # digit1 =2*10**0+ 5*10**0
    # assert digit1 == 7
    # print(n1)
    # print(n2)
    # print(n1+n2)
