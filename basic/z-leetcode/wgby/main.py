'''
输入n，打印一个n*n的Z型矩阵
例如：n = 4
打印：
1 2 6 7
3 5 8 13
4 9 12 14
10 11 15 16
'''
def generate_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    slopes = 2 * n - 1
    
    for slope in range(slopes):
        if slope % 2 == 0:  # Even slope
            for i in range(n):
                j = slope - i
                if 0 <= j < n:
                    matrix[i][j] = num
                    num += 1
        else:  # Odd slope
            for i in range(n-1, -1, -1):
                j = slope - i
                if 0 <= j < n:
                    matrix[i][j] = num
                    num += 1
    return matrix

# Testing the function
for row in generate_matrix(4):
    print(row)
