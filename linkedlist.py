from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val: int = val
        self.next: Optional[ListNode] = next


def linked_list_to_array(cur: Optional[ListNode], ar: List[int] = None) -> List[int]:
    if ar is None:
        ar = list()
    if cur is None:
        return ar
    ar.append(cur.val)
    # print("to array", cur.val)
    return linked_list_to_array(cur.next, ar)


def linked_list_from_array(ar: List[int]) -> ListNode:
    head = ListNode()
    size = len(ar)
    # print(size, ar)
    cur: ListNode = head
    index = 0
    while index < size:
        cur.val = ar[index]
        # print(index, cur.val)
        index += 1
        if index < size:
            cur.next = ListNode()
            cur = cur.next
    return head


def int_to_linked_list(n: int) -> ListNode:
    head = ListNode()
    cur = head
    import pdb

    pdb.set_trace()
    while n > 0:
        cur.val = n % 10
        oldn = n
        n = int(n / 10)
        assert n * 10 == oldn
        if n > 0:
            cur.next = ListNode()
            cur = cur.next
    return head
