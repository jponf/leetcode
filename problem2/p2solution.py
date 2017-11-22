#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ListNode:

    @staticmethod
    def from_list(lst):
        if lst:
            current = first = ListNode(lst[0])
            for i in lst[1:]:
                current.next = ListNode(i)
                current = current.next
            return first
        else:
            return ListNode(0)

    """Definition for singly-linked list."""
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        current, text = self, "["
        while current:
            text += str(current.val)
            current = current.next
            if current:
                text += ","
        return text + "]"


def add_two_numbers(lst1, lst2):
    """
    You are given two non-empty linked lists representing two non-negative
    integers. The digits are stored in reverse order and each of their nodes
    contain a single digit. Add the two numbers and return it as a linked
    list.

    You may assume the two numbers do not contain any leading zero, except
    the number 0 itself.

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8

    :type lst1: ListNode
    :type lst2: ListNode
    :rtype: ListNode
    """
    current = dummy = ListNode(0)
    val = 0

    while lst1 and lst2:
        val = lst1.val + lst2.val + val // 10
        current.next = ListNode(val % 10)
        lst1, lst2, current = lst1.next, lst2.next, current.next

    remaining = lst1 if lst1 is not None else lst2
    while remaining:
        val = remaining.val + val // 10
        current.next = ListNode(val % 10)
        current, remaining = current.next, remaining.next

    if val // 10 > 0:
        current.next = ListNode(val // 10)

    return dummy if dummy.next is None else dummy.next


if __name__ == '__main__':
    lst1 = ListNode.from_list([2, 4, 3])
    lst2 = ListNode.from_list([5, 6, 4])

    print(lst1, "+", lst2, "=", add_two_numbers(lst1, lst2))
