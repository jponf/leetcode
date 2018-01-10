#!/usr/bin/env python3

import itertools
import timeit


def max_island_area1(grid):
    displacements = ((1, 0), (-1, 0), (0, 1), (0, -1))
    len_r, len_c = len(grid), len(grid[0])

    m_area, seen = 0, set()
    for i, j in itertools.product(range(len_r), range(len_c)):
        if grid[i][j] == 1 and (i, j) not in seen:
            stack, area = [(i, j)], 1
            seen.add((i, j))
            while stack:
                r, c = stack.pop()
                for dr, dc in displacements:
                    nr = r + dr
                    nc = c + dc
                    if (nr, nc) not in seen \
                            and 0 <= nr < len_r and 0 <= nc < len_c \
                            and grid[nr][nc] == 1:
                        area += 1
                        seen.add((nr, nc))
                        stack.append((nr, nc))
            m_area = max(m_area, area)

    return m_area


def getmax(grid, i, j):  # make it iterative
    grid[i][j] = -1
    count = 1
    if i > 0 and grid[i - 1][j] == 1:
        count += getmax(grid, i - 1, j)
    if j > 0 and grid[i][j - 1] == 1:
        count += getmax(grid, i, j - 1)
    if i + 1 < len(grid) and grid[i + 1][j] == 1:
        count += getmax(grid, i + 1, j)
    if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
        count += getmax(grid, i, j + 1)
    return count


def max_island_area2(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m = 0
    for i, r in enumerate(grid):
        for j, v in enumerate(r):
            if v == 1:
                m = max(m, getmax(grid, i, j))
    return m


if __name__ == '__main__':
    islands1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,1,1,0,1,0,0,0,0,0,0,0,0],
                [0,1,0,0,1,1,0,0,1,0,1,0,0],
                [0,1,0,0,1,1,0,0,1,1,1,0,0],
                [0,0,0,0,0,0,0,0,0,0,1,0,0],
                [0,0,0,0,0,0,0,1,1,1,0,0,0],
                [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    islands2 = [[0,0,0,0,0,0,0,0]]
    islands3 = [[0,0,0,0,1,0,0,0],
                [0,0,0,0,1,0,0,0]]

    def time_fn(max_island_fn, grid):
        def fn():
            max_island_fn(islands1)

        return timeit.timeit(fn, number=100000)

    # print("Time Area1 1:", time_fn(max_island_area1, islands1))
    # print("Time Area1 2:", time_fn(max_island_area1, islands2))
    # print("Time Area1 3:", time_fn(max_island_area1, islands3))

    #print("Time Area2 1:", time_fn(max_island_area2, islands1))
    #print("Time Area2 2:", time_fn(max_island_area2, islands2))
    #print("Time Area2 3:", time_fn(max_island_area2, islands3))

    print("Area1 1:", max_island_area1(islands1))
    print("Area1 2:", max_island_area1(islands2))
    print("Area1 3:", max_island_area1(islands3))

    print("Area2 1:", max_island_area2(islands1))
    print("Area2 2:", max_island_area2(islands2))
    print("Area2 3:", max_island_area2(islands3))