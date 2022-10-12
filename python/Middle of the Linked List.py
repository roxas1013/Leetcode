class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        le = ri = head
        while ri and ri.next:
            le = le.next
            ri = ri.next.next
        return le
        
