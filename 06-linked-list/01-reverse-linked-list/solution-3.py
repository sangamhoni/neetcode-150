# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # My own solution: Iterative process
        
        if not head:
            return head

        node = ListNode(head.val)
        curr = head.next

        while curr:
            new_node = ListNode(curr.val)
            new_node.next = node
            node = new_node

            curr = curr.next
        
        return node
        