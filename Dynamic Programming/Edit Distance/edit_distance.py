# python3


def edit_distance(first_string, second_string):
    n, m = len(first_string), len(second_string)
    d = []
    for row in range(n+1):
        r = []
        for column in range(m+1):
            if row == 0:
                r.append(column)
            elif column == 0:
                r.append(row)
            else:
                r.append(0)
        d.append(r)
    for i in range(1, n+1):
        for j in range(1, m+1):
            if first_string[i-1] == second_string[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = min(d[i-1][j] + 1, d[i][j-1] + 1, d[i-1][j-1]+1)
    print(d)
    return d[n][m]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
