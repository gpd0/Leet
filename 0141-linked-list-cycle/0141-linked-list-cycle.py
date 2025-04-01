# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if not head.next:
            return False
        hashMap = {}
        curr_node = head
        while curr_node:
            hashMap[curr_node] = curr_node.next
            if curr_node.next in hashMap:
                return True
            curr_node = curr_node.next
        return False

        