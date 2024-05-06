# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p = head
        q = head
        if p != None:
            p = p.next
        else:
            return False
        
        if q != None and q.next != None:
            q = q.next.next
        else:
            return False
 
        while p != None and q != None:
            p = p.next
            if q.next != None:
                q = q.next.next
            if p != None and q != None and p == q:
                return True
        return False
    
    
    