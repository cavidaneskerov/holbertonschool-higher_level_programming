#!/usr/bin/python3
"""Pascal's Triangle function"""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle of n"""
    if n <= 0:
        return []

    triangle = [[1]]  # İlk sətr

    for i in range(1, n):
        prev_row = triangle[i - 1]
        row = [1]  # Sətrin ilk elementi həmişə 1

        # Orta elementləri hesabla
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)  # Sətrin son elementi həmişə 1
        triangle.append(row)

    return triangle
