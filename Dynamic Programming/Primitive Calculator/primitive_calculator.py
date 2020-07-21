# python3
import sys

def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    ways = [[], [1]]
    for num in range(2, n+1):
        min1 = len(ways[num-1]) - 1
        min2 = sys.maxsize
        min3 = sys.maxsize
        if num % 3 == 0:
            min3 = len(ways[num//3]) - 1
        if num % 2 == 0:
            min2 = len(ways[num//2]) - 1
        # print("Num:{} min1:{} min2:{} min3:{}".format(num, min1, min2, min3))
        minways = min(min3, min2, min1)
        if minways == min3:
            steps = ways[num//3] + [num]
        elif minways == min2:
            steps = ways[num // 2] + [num]
        elif minways == min1:
            steps = ways[num - 1] + [num]
        ways.append(steps)
    return ways[n]

if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)

