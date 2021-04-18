# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        current1 = l1
        current2 = l2
        
        new_head = ListNode()
        current = new_head
        carry = 0
        while current1 or current2:
            temp = carry
            temp += current1.val if current1 else 0
            temp += current2.val if current2 else 0
            
            sum = temp % 10
            carry = temp // 10
            
            current.next = ListNode(sum)
            current = current.next
            
            current1 = current1.next if current1 else None
            current2 = current2.next if current2 else None
            
        if carry:
            current.next = ListNode(carry)
            
        return new_head.next

def get_list(num):
    head = ListNode(num[-1])
    for n in num[:-1][::-1]:
        temp = ListNode(n, head)
        head = temp
        
    return head

def print_list(head: ListNode):
    current = head
    while current:
        print(current.val)
        current = current.next

solution = Solution()
print_list(solution.addTwoNumbers(get_list([2, 4, 3]), get_list([5, 6, 4])))
print_list(solution.addTwoNumbers(get_list([0]), get_list([0])))
print_list(solution.addTwoNumbers(get_list([5]), get_list([5])))
print_list(solution.addTwoNumbers(get_list([9]), get_list([9])))
print_list(solution.addTwoNumbers(get_list([9, 9, 9, 9, 9, 9, 9]), get_list([9, 9, 9, 9])))