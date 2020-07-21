# python3

# You can solve the problem analytically. If the number you're trying to reach is N, then the answer will always be
#
# 1+2+3+ ... +n + r = N
# where n is the largest possible number such that n < r. For example, take N=8, and consider the possible values of n
#
# n   sum(1..n)  r
# 0       0      8
# 1       1      7
# 2     1+2=3    5
# 3    1+2+3=6   2    // too high, n is not less than r
# Thus, when N is 8, n is 2 and r is 5, giving an answer of 1+2+5.
#
# So the question becomes, given the value of N, how can we compute n. The first step is to note that the sum of 1 thru n is given by the equation
#
# 1+2+3+ ... +n = n(n+1)/2
# Plug that into the first equation
#
# n(n+1)/2 + r = N
# Using the fact that n < r, we can rewrite this as
#
# n(n+1)/2 + n < N
# n < (-3 + sqrt(9 + 8N))/2
# And that's the answer that you need to implement.
# For example, if N is 2, then the formula says n < 1 which means that n is 0 and r is 2.
# If N is 8, then n < 2.77, which means that n is 2 and r is 5.

import math

def compute_optimal_summands(N):
    assert 1 <= N <= 10 ** 9
    c = (-3 + math.sqrt(9 + 8*N))/2
    c = math.ceil(c-1)
    summands = [i for i in range(1,c+1)]
    summands.append(N-sum(summands))
    return summands



if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
