from linkedlist import *
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
      #list1: 1,2,3
      #list2  2,3,4
      #i = 0
      #ch1 = 1
      #ch2 = 2
      #ch1 < ch2
      #   append(ch1)
      #    list1=list1.next()

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      if not list1 and not list2:
          return None
      if not list1:
          return list2
      if not list2:
          return list1
      head = cur = None
      while list1 and list2:  ## t t
          if list1.val <= list2.val:## 1 < 2
             # append list1 to cur   
             if cur is None: ## t
                 cur = head = ListNode(list1.val) # 1
             else:
                 cur.next = ListNode(list1.val)
                 cur = cur.next
             list1 = list1.next 
          else:  # list1 > list2
             # append list2 to cur
             if cur is None:
                 cur = head = ListNode(list2.val)
             else:
                 cur.next = ListNode(list2.val)
                 cur = cur.next
             list2 = list2.next 
      while list1:
         if cur is None:
             cur = head = ListNode(list1.val)
         else:
             cur.next = ListNode(list1.val)
             cur = cur.next
             list1 = list1.next 
      while list2:
         if cur is None:
             cur = head = ListNode(list2.val)
         else:
             cur.next = ListNode(list2.val)
             cur = cur.next
             list2 = list2.next 
      return head
solution = Solution()
if __name__ == "__main__":
    #l1 = linked_list_from_array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
    #l2 = linked_list_from_array([5, 6, 4])
    #solution.debug_add( l1, l2, [6, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])

    #l1 = linked_list_from_array([2, 4, 3])
    #l2 = linked_list_from_array([5, 6, 4])
    #solution.debug_add( l1, l2, [7, 0, 8])

    l1 = linked_list_from_array([2,4,6])
    l2 = linked_list_from_array([1,3,5,7,9])
    lans =solution.mergeTwoLists( l1, l2) 
    ans= linked_list_to_array(lans)
    print(ans)
    assert ans == [1,2,3,4,5,6,7,9]
    # n1 = 2*10**0  + 4*10**1 + 3*10**2
    # n2 = 5*10**0  + 6*10**1 + 4*10**2
    # digit1 =2*10**0+ 5*10**0
    # assert digit1 == 7
    # print(n1)
    # print(n2)
    # print(n1+n2)
