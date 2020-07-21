def min_groups(n, ages):
    ages = sorted(ages, reverse = True)
    groups = []
    i = 0
    while i <= n-1:
        curr = ages[i]
        l = []
        while i <= n-1 and curr - ages[i] <= 1:
            l.append(ages[i])
            i += 1
        groups.append(l)
    return groups


n = int(input())
ages = [float(x) for x in input().split()]
print(min_groups(n, ages))