from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if head == None:
            return None

        i = 1
        p = head
        p_pre = None
        while  p != None and i < left:
            p_pre = p
            p = p.next
            i += 1
        
        # 头插法将p_next和p交换位置
        h = p_pre
        p_pre.next = None
        tail = None
        while p != None and i <= right:
            if i == left:
                tail = p
            # 保存指针
            h_next = h.next
            p_next = p.next

            # 头插法
            h.next = p
            p.next = h_next
            p = p_next
            i += 1
        
        if p != None and tail != None:
            tail.next = p
        return head
  
def printList(head):
    p = head
    while p != None:
        print(p.val)
        p = p.next
        

if __name__ == '__main__':
    solution = Solution()
    
    head = [1,2,3,4,5]
    left = 2
    right = 4
    
    p = ListNode()
    h = p
    for i in head:
        node = ListNode(i)
        p.next = node
        p = p.next
        
    printList(h.next)
    print("------")
    head2 = solution.reverseBetween(h.next,2,4) 
    printList(head2) # 1 4 3 2 5