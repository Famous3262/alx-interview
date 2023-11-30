#!/usr/bin/python3
"""Pascal triangle interview"""

def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = [0] * n
    
    for i in range(n):
        row = [0] * (i+1)
        row[0] = 1
        row[len(row) - 1] = 1
        
        for j in range(1, i):
            if j > 0 and j < len(row):
                a = triangle[i - 1][j]
                b = triangle[i - 1][j - 1]
                row[j] = a + b
        
        triangle[i] = row
    
    return triangle
