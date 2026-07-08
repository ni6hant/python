# Write your solution here

def block_correct(sudoku: list, row_no: int, column_no: int):
    check=[]
    i=0
    j=0
    #elements start from 0,0 to 0+2,0+2 included or 0+3), 0+3)
    for row in sudoku:
        if row[column_no] in check and row[column_no]>0:
            return False
        else:
            check.append(row[column_no])
    return True

if __name__ == "__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))