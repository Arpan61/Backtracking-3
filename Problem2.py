class Solution:
    def exist(self, board, word) -> bool:
        rows = len(board)
        cols = len(board[0])

        def backtracking(r, c, currindex):
            if currindex == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or word[currindex] != board[r][c]:
                return False
            if board[r][c] == word[currindex]:
                # print(r,c, board[r][c])
                temp = board[r][c]
                board[r][c] = '#'
            res = backtracking(r - 1, c, currindex + 1) or backtracking(r + 1, c, currindex + 1) \
                  or backtracking(r,c - 1,currindex + 1) or backtracking(r, c + 1, currindex + 1)
            board[r][c] = temp
            return res

        for r in range(rows):
            for c in range(cols):
                if backtracking(r, c, 0) is True:
                    return True

        return False