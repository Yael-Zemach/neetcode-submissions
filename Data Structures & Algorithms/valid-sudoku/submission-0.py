class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            array = [0]*10
            for j in range(len(board[0])):
                if board[i][j]!=".":
                    if array[int(board[i][j])]:
                        return False
                    array[int(board[i][j])] = 1
        for i in range(len(board[0])):
            array = [0]*10
            for j in range(len(board)):
                if board[j][i]!=".":
                    if array[int(board[j][i])]:
                        return False
                    array[int(board[j][i])] = 1
        for k in range(9):
            array = [0]*10
            startR = (k//3)*3
            startC = (k%3)*3
            for c in range(3):
                for r in range(3):
                    val = board[startR + r][startC + c]
                    if val !=".":
                        if array[int(val)]:
                            return False
                        array[int(val)] = 1


        return True





        
        
    


        
                
        
                    
                
        

        

        


        