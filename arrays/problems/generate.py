class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        ls = [[1],[1,1]]
        innerls = []
        i = 2
        while i < numRows:
            innerls = [0]* (i+1)
            j = 0
            while j < i+1:
                if j==0 or j==i: innerls[j] = 1
                else:
                    innerls[j] = ls[i-1][j-1] + ls[i-1][j]
                j+=1 
            ls.append(innerls)     
            i+=1
        return ls

        