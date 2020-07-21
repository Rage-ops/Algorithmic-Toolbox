# python3
from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return ((first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2)**0.5


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared

def hybrid_min(left_points, right_points, line_strip, width):
    left = []
    for pt in left_points:
        if abs(pt.x - line_strip) <= width:
            left.append(pt)
    right = []
    for pt in right_points:
        if abs(pt.x - line_strip) <= width:
            right.append(pt)
    total = left+right
    total = sorted(total, key=lambda p: p.y)
    # print("Total : {}".format(total))
    result = width
    for i in range(len(total)):
        for j in range(i + 1, min(i + 8, len(total))):
            if abs(total[i].y - total[j].y) <= width:
                result = min(result, distance_squared(total[i], total[j]))
    return result


def minimum_distance_squared(points, n):
    # print(points)
    if n <= 3:
        return minimum_distance_squared_naive(points)
    pts_l = points[:n//2]
    pts_r = points[n//2:]
    min_l = minimum_distance_squared(pts_l, n//2)
    min_r = minimum_distance_squared(pts_r, n - n//2)
    seperate_min = min(min_l, min_r)
    strip_l = (pts_l[-1].x + pts_r[0].x)//2
    # print("sep_min : {}, strip_l :{}".format(seperate_min, strip_l))
    hybridmin = hybrid_min(pts_l, pts_r, strip_l, seperate_min)
    return min(seperate_min, hybridmin)


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)
    sorted_pts = sorted(input_points, key=lambda pt: pt.x)
    print("{:.4f}".format(minimum_distance_squared(sorted_pts, input_n)))
    # print("{0:.9f}".format(sqrt(minimum_distance_squared_naive(input_points))))
