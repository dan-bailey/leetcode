# it feels like there's a more elegant way to do this

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        target = [head]
        while target[-1].next:
            target.append(target[-1].next)
        return target[len(target) // 2]