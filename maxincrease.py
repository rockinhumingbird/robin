  
  
grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        
        rowMax=[0]*m
        colMax=[0]*n
        
        for i in range(m):
            rowMax[i]=max(grid[i][:])
        
        for j in range(n):
            tmp=list()
            for i in range(m):
                tmp.append(grid[i][j])
            colMax[j]=max(tmp)
        
        total=0
        
        for i in range(m):
            for j in range(n):
                total+=min(colMax[j]-grid[i][j],rowMax[i]-grid[i][j])
        return total

def maxIncreaseKeepingSkyline(self, grid):
       rows, cols = list(map(max, grid)), list(map(max, zip(*grid)))
       return sum(min(i, j) for i in rows for j in cols) - sum(map(sum, grid))

def maxIncreaseKeepingSkyline(self, grid):
        rows_max = [0] * len(grid)
        cols_max = [0] * len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                rows_max[i] = max(rows_max[i], grid[i][j])
                cols_max[j] = max(cols_max[j], grid[i][j])

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += min(rows_max[i], cols_max[j]) - grid[i][j]

        return res