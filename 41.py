class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l1 
        nt = 0
        sum_ = 0
        
        while l1 and l2:
            sum_ = l1.val + l2.val + nt
            l1.val = sum_ % 10
            nt = 1 if sum_ > 9 else 0 
            
            if not l1.next and l2.next:
                l1.next = ListNode()
            if l1.next and not l2.next: 
                l2.next = ListNode()
            if not l1.next and not l2.next: 
                if nt:
                    l1.next = ListNode(val=1)
                    nt = 0
                            
            l1, l2 = l1.next, l2.next
            
        return head
