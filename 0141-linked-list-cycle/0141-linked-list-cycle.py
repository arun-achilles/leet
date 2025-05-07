# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_map = {}
        curr = head
        idx = 0 
        while curr:
            if curr in visited_map:
                return True #visited_map[curr]
            visited_map[curr] = idx
            idx += 1
            curr = curr.next
        return False
