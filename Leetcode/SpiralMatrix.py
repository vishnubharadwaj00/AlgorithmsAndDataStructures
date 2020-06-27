def spiral(matrix):
    ans = []

    def sp(r1, c1, r2, c2):
        for i in range(c1, c2+1):
            yield r1, i
        for i in range(r1+1, r2+1):
            yield i, c2
        if (r1 < r2 and c1 < c2):
            for i in range(c2-1, c1, -1):
                yield r2, i
            for i in range(r2, r1, -1):
                yield i, c1

    if not matrix:
        return []
    r1, r2 = 0, len(matrix)-1
    c1, c2 = 0, len(matrix[0]) - 1
    while r1 <= r2 and c1 <= c2:
        for r, c in sp(r1, c1, r2, c2):
            ans.append(matrix[r][c])
        r1 += 1
        r2 -= 1
        c1 += 1
        c2 -= 1
    return ans


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

x = spiral(matrix)
print(x)
