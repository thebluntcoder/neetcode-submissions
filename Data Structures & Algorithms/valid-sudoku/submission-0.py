class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if (val in rows[i] or
                    val in cols[j] or
                    val in squares[(i//3, j//3)]):
                    return False
                    print("Row : ", rows)
                    print("Col : ", cols)
                    print("Squares : ", squares)
                cols[j].add(val)
                rows[i].add(val)
                squares[(i//3, j//3)].add(val)
                print("Row : ", rows)
                print("Col : ", cols)
                print("Squares : ", squares)
        return True