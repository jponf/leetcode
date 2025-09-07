"""Given the head of a linked list, remove the nth node from the end
of the list and return its head.

Example 1:
    Input: head = [1,2,3,4,5], n = 2
        1 -> 2 -> 3 -> 4 -> 5
    Output: [1,2,3,5]
        1 -> 2 -> 3 -> 5

Example 2:
    Input: head = [1], n = 1
    Output: []

Example 3:
    Input: head = [1,2], n = 1
    Output: [1]

Constraints:
    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        prev_n = None
        del_n = head
        node_it = head
        count = 0

        while node_it is not None and count < n:
            node_it = node_it.next
            count += 1
        while node_it is not None:
            node_it = node_it.next
            prev_n = del_n
            del_n = del_n.next

        if prev_n is None:  # remove head
            return del_n.next

        prev_n.next = del_n.next
        return head


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5]
    n = 2

    # Make list
    head = ListNode(values[-1])
    for i in range(len(values) - 2, -1, -1):
        head = ListNode(values[i], next=head)

    # Run solution
    solution = Solution()
    s_head = solution.removeNthFromEnd(head, n)

    # Output
    node = s_head
    s_values = []
    while node is not None:
        s_values.append(node.val)
        node = node.next
    print(s_values)
