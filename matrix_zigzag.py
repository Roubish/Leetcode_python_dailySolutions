# Matrix Zigzag with Obstacles and Variable Steps

# You are given an m x n integer matrix grid. You start at any cell in the first row.

# 1. At each step, you move to the next row.

# 2. You can move at most k columns left or right from your current column.

# 3. Some cells are obstacles (represented by -1) and cannot be stepped on.

# 4. Collect the sum of numbers along your path.

# Return the maximum sum you can collect from top to bottom. If no valid path exists, return -1.
'''
    Input: grid = [
    [1, 2, 3],
    [4, -1, 6],
    [7, 8, 9]
    ], k = 1
    Output: 18

    Explanation:
    One optimal path: 
    - Start at 2 (row 0, col 1) 
    - Move to 4 (row 1, col 0) [can move max 1 left/right] 
    - Move to 9 (row 2, col 2) 
    Sum = 2 + 4 + 9 = 15

    Another path: 
    - Start at 3 (row 0, col 2) 
    - Move to 6 (row 1, col 2) [ok, within k=1] 
    - Move to 9 (row 2, col 2) 
    Sum = 3 + 6 + 9 = 18 
    
'''

def maxZigzagSumWithObstacles(grid, k):
    m, n = len(grid), len(grid[0])
    dp = [-float('inf')] * n
    
    for j in range(n):
        if grid[0][j] != -1:
            dp[j] = grid[0][j]
            
    for i in range(1, m):
        new_dp = [-float('inf')] * n 
        for j in range(n):
            if grid[i][j] == -1:
                continue
            for x in range(max(0, j-k), min(n, j+k+1)):
                if dp[x] != -float('inf'):
                    new_dp[j] = max(new_dp[j], dp[x] + grid[i][j])
        dp = new_dp
    max_sum = max(dp)
    return max_sum if max_sum != -float('inf') else -1

grid = [
  [1, 2, 3],
  [4, -1, 6],
  [7, 8, 9]
]
k = 1
print("============output============")
print("m x n integer matrix grid",maxZigzagSumWithObstacles(grid, k))

# ghost@ghost-GF65-Thin-10UE:~/Documents/program_txt_folder/dsa_code$ python3 matrix_zigzag.py 
# ============output============
# 18