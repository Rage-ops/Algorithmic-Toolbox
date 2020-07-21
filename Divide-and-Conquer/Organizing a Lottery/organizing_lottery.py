# python3
from sys import stdin
from bisect import bisect_left, bisect_right


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


def points_cover(starts, ends, points):
    leftpts = list(zip(starts, ['left']*n))
    rightpts = list(zip(ends, ['right']*n))
    pts = list(zip(points, ['pt']*m))
    l = sorted(leftpts+rightpts+pts, key = lambda item: (item[0], item[1][0]))
    # print(l)
    res = {}
    for p in points:
        res[p] = 0
    left_count = 0
    for i in l:
        if i[1] == 'left':
            left_count += 1
        elif i[1] == 'right':
            left_count -= 1
        elif i[1] == 'pt':
            res[i[0]] = left_count
    out = []
    for p in points:
        out.append(res[p])
    return out


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]
    # input_starts = []
    # input_ends = []
    # n, m = map(int, input().split())
    # for i in range(n):
    #     left, right = map(int, input().split())
    #     input_starts.append(left)
    #     input_ends.append(right)
    # input_points = [int(x) for x in input().split()]
    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)
