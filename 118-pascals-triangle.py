def generateTri(numRows):
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1, 1]]
    else:
        tri = [[1], [1, 1]]
        for i in range(2, numRows):
            row = [1]
            for j in range(1, i):
                row.append(tri[i-1][j-1] + tri[i-1][j])
            row.append(1)
            tri.append(row)
        return tri