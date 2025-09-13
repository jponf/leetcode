"""You are given an array of k linked-lists lists, each linked-list is
sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
    Explanation: The linked-lists are:
        [
            1->4->5,
            1->3->4,
            2->6
        ]
        merging them into one sorted linked list:
        1->1->2->3->4->4->5->6

Example 2:
    Input: lists = []
    Output: []

Example 3:
    Input: lists = [[]]
    Output: []

Constraints:
    k == lists.length
    0 <= k <= 104
    0 <= lists[i].length <= 500
    -104 <= lists[i][j] <= 104
    lists[i] is sorted in ascending order.
    The sum of lists[i].length will not exceed 104.
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self._merge_k(lists, 0, len(lists) - 1) if lists else None

    def _merge_k(
        self,
        lists: List[Optional[ListNode]],
        left: int,
        right: int,
    ) -> Optional[ListNode]:
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2

        l_list = self._merge_k(lists, left, mid)
        r_list = self._merge_k(lists, mid + 1, right)
        return self._merge_two(l_list, r_list)

    def _merge_two(
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
    lists_values = [[1, 4, 5], [1, 3, 4], [2, 6]]
    # Expected [1, 1, 2, 3, 4, 4, 5, 6]

    # Make list
    lists = [_make_linked_list(values) for values in lists_values]

    # Run solution
    solution = Solution()
    merged = solution.mergeKLists(lists)

    # Output
    node = merged
    s_values = []
    while node is not None:
        s_values.append(node.val)
        node = node.next
    print("Merged:", s_values)
