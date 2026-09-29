# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #reversing means making each pointer point the opposite direction
        # starting from the back each pointer points backward to the one who called it 
        if not head:
            return None
        newhead = head
        if head.next:
            newhead = self.reverseList(head.next) #recursively call the function
            head.next.next = head #the next node's pointer points to the current node
        head.next = None #the head's pointer points to none after reversal

        return newhead