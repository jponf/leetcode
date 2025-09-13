"""You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by
splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

Example 2:
    Input: list1 = [], list2 = []
    Output: []

Example 3:
    Input: list1 = [], list2 = [0]
    Output: [0]

Constraints:
    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode],
    ) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next

            node = node.next

        node.next = list1 or list2
        return dummy.next


def _make_linked_list(values: list[int]) -> Optional[ListNode]:
    if not values:
        return None

    head = ListNode(values[-1])
    for i in range(len(values) - 2, -1, -1):
        head = ListNode(values[i], next=head)
    return head


if __name__ == "__main__":
    list1_values = [1, 2, 4]
    list2_values = [1, 3, 4]

    # Make list
    list1 = _make_linked_list(list1_values)
    list2 = _make_linked_list(list2_values)

    # Run solution
    solution = Solution()
    merged = solution.mergeTwoLists(list1, list2)

    # Output
    node = merged
    s_values = []
    while node is not None:
        s_values.append(node.val)
        node = node.next
    print("Merged:", s_values)
