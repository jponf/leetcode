"""Given a linked list, swap every two adjacent nodes and
return its head. You must solve the problem without modifying
the values in the list's nodes (i.e., only nodes themselves may
be changed.)

Example 1:
    Input: head = [1,2,3,4]
    Output: [2,1,4,3]

Example 2:
    Input: head = []
    Output: []

Example 3:
    Input: head = [1]
    Output: [1]

Example 4:
    Input: head = [1,2,3]
    Output: [2,1,3]

Constraints:
    The number of nodes in the list is in the range [0, 100].
    0 <= Node.val <= 100
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # return self._swap_rec(head)
        return self._swap_rec(head)

    def _swap_rec(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            if head.next is None:
                return head

            next_n = head.next
            head.next = self.swapPairs(next_n.next)
            next_n.next = head

            return next_n

    def _swap_it(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        stack = []
        node: Optional[ListNode] = head
        while node is not None:
            print(node.val)
            stack.append((node, node.next))
            if node.next is not None:
                node = node.next.next
            else:
                node = None

        stack_ret: Optional[ListNode] = None
        while stack:
            node, next_n = stack.pop()
            print(
                node.val,
                next_n.val if next_n else None,
                stack_ret.val if stack_ret else None,
            )
            if next_n is None:
                stack_ret = node
            else:
                node.next = stack_ret
                next_n.next = node
                stack_ret = next_n
        return stack_ret


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


if __name__ == "__main__":
    list_values = [1, 2, 3, 4, 5]

    # Make list
    lists = _make_linked_list(list_values)

    # Run solution
    solution = Solution()
    merged = solution.swapPairs(lists)

    # Output
    node = merged
    s_values = []
    while node is not None:
        s_values.append(node.val)
        node = node.next
    print("Merged:", s_values)
