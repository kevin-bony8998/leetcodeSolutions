# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverseNodes(nodeStart, nodeEnd):
            if not nodeStart:
                return (None, None)
            elif nodeStart == nodeEnd:
                return (nodeEnd, nodeEnd)
            returnedNodes = reverseNodes(nodeStart.next, nodeEnd)
            returnedNodes[1].next = nodeStart
            nodeStart.next = None
            return (returnedNodes[0], nodeStart)
            
        ans = ListNode()
        dupAns = ans
        count = 0
        dup = head
        while head:
            count += 1
            if count == k:
                count = 0
                headNext = head.next
                returnedNodes = reverseNodes(dup, head)
                ans.next = returnedNodes[0]
                ans = returnedNodes[1]
                head = headNext
                dup = head
            else:
                head = head.next
        if count > 0:
            ans.next = dup
        return dupAns.next
        