#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def length_of_longest_substring(text):
    chars = {}  # type: MutableMapping[str, int]
    best, first = 0, 0

    for i, c in enumerate(text):
        if c in chars:
            best = max(best, i - first)
            first = max(first, chars.pop(c) + 1)
        chars[c] = i

    return max(best, len(text) - first)


if __name__ == '__main__':
    text = "abcabcbb"

    print("Length of longest substring in '%s'" % text)
    print(length_of_longest_substring(text))
