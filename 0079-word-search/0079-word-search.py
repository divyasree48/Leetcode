class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r=len(board)
        c=len(board[0])
        def fun(i,j,lenn):
            if lenn==len(word):
                return 1
            if i<0 or i>r-1 or j<0 or j>c-1 or board[i][j]!=word[lenn]:
                return 0
            a=board[i][j]
            board[i][j]='!'
            if(fun(i-1,j,lenn+1)):
                return 1
            if(fun(i+1,j,lenn+1)):
                return 1
            if fun(i,j-1,lenn+1):
                return 1
            if fun(i,j+1,lenn+1):
                return 1
            board[i][j]=a
            return 0
        for i in range(r):
            for j in range(c):
                if fun(i,j,0):
                    return 1
        return 0