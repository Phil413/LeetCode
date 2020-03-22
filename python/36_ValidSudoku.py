class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in board:
            check_map = {str(e): 0 for e in range(1, 10)}
            for j in i:
                if j in check_map:
                    check_map[j] += 1
                    if check_map[j] > 1:
                        return False
        for i in zip(*board):
            check_map = {str(e): 0 for e in range(1, 10)}
            for j in i:
                if j in check_map:
                    check_map[j] += 1
                    if check_map[j] > 1:
                        return False
        for i in range(0, 3):
            for j in range(0, 3):
                tmp_nums = board[i*3][j*3:(j+1)*3] + board[i*3+1][j*3:(j+1)*3] + board[i*3+2][j*3:(j+1)*3]
                check_map = {str(e): 0 for e in range(1, 10)}
                for z in tmp_nums:
                    if z in check_map:
                        check_map[z] += 1
                        if check_map[z] > 1:
                            return False
        return True

    def isValidSudoku2(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        boxes = [{} for _ in range(9)]
        
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val != '.':
                    num = int(val)
                    rows[row][num] = rows[row].get(num, 0) + 1
                    cols[col][num] = cols[col].get(num, 0) + 1
                    box = (row // 3) * 3 + col // 3
                    boxes[box][num] = boxes[box].get(num, 0) + 1
                    if rows[row][num] > 1 or cols[col][num] > 1 or boxes[box][num] > 1:
                        return False

if __name__ == "__main__":
	board = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
	sl = Solution()
	print(sl.isValidSudoku2(board))