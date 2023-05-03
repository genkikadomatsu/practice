from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        for x in range(9):
            for y in range(9):
                
                curr_num = board[x][y]

                if curr_num == ".":
                    continue
                
                if curr_num in rows[x] or curr_num in cols[y] or curr_num in boxes[(x//3, y//3)]:
                    return False

                rows[x].add(curr_num)
                cols[y].add(curr_num)
                boxes[(x//3, y//3)].add(curr_num)

        
        return True


