"""Given the head of a linked list, reverse the nodes of the list k at
a time, and return the modified list.

K is a positive integer and is less than or equal to the length of the
linked list. If the number of nodes is not a multiple of k then left-out
nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves
may be changed.

Example 1:
    Input: head = [1,2,3,4,5], k = 2
    Output: [2,1,4,3,5]

Example 2:
    Input: head = [1,2,3,4,5], k = 3
    Output: [3,2,1,4,5]

Constraints:
    The number of nodes in the list is n.
    1 <= k <= n <= 5000
    0 <= Node.val <= 1000

Follow-up: Can you solve the problem in O(1) extra memory space?
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new_h = None
        tail = None
        group_h = None

        curr_n = head
        prev_n = None
        next_n = None

        count = 0
        while curr_n is not None:
            if count % k == 0:
                if tail is not None:
                    tail.next = prev_n
                if new_h is None:
                    new_h = prev_n

                tail = group_h
                prev_n = None
                group_h = curr_n

            count = count + 1

            # Reverse
            next_n = curr_n.next
            curr_n.next = prev_n
            prev_n = curr_n
            curr_n = next_n

        if tail is not None:
            tail.next = prev_n
        if new_h is None:
            new_h = prev_n

        # Undo last group because it does not have K elements
        if count % k > 0:
            if tail is not None:
                tail.next = group_h
            if new_h is None:
                new_h = head

            curr_n = prev_n
            prev_n = None
            while curr_n is not None:
                next_n = curr_n.next
                curr_n.next = prev_n
                prev_n = curr_n
                curr_n = next_n

        return new_h


###############
## Utilities ##
###############


def _make_linked_list(values: list[int]) -> Optional[ListNode]:
    if not values:
        return None

    head = ListNode(values[-1])
    for i in range(len(values) - 2, -1, -1):
        head = ListNode(values[i], next=head)
    return head


def _get_linked_list_values(head: Optional[ListNode]) -> List[int]:
    node = head
    s_values = []
    while node is not None:
        s_values.append(node.val)
        node = node.next

    return s_values


if __name__ == "__main__":
    list_values = [1, 2, 3, 4, 5]
    k = 3

    # Make list
    head = _make_linked_list(
        list_values,
    )

    # Run solution
    solution = Solution()
    reversed = solution.reverseKGroup(head, k)

    # Output
    s_values = _get_linked_list_values(reversed)
    print(f"Reversed({k}):", s_values)
