import numpy as np

def solve_sudoku(grid):
    """
    数独を解くメイン関数
    """
    
    # 空のセルを見つける
    empty = find_empty(grid)
    
    if not empty:
        return True  # パズルが解けた
    
    row, col = empty
    
    # 1から9までの数字を試す
    for num in range(1, 10):
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num
            
            if solve_sudoku(grid):
                return True
            
            grid[row][col] = 0  # バックトラック
    
    return False  # 解が見つからない

def find_empty(grid):
    """
    空のセル（値が0）を見つける
    """
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def is_valid(grid, num, pos):
    """
    指定された位置に数字を配置できるかチェック
    """
    grid_np = np.array(grid)
    # 行をチェック
    if num in grid_np[pos[0]]:
        return False
    
    # 列をチェック
    if num in grid_np[:, pos[1]]:
        return False
    
    # 3x3のボックスをチェック
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if grid[i][j] == num:
                return False
    
    return True

def print_grid(grid):
    """
    数独のグリッドを表示
    """
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            
            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")

# 使用例
if __name__ == "__main__":
    # grid = [
    #     [5, 3, 0, 0, 7, 0, 0, 0, 0],
    #     [6, 0, 0, 1, 9, 5, 0, 0, 0],
    #     [0, 9, 8, 0, 0, 0, 0, 6, 0],
    #     [8, 0, 0, 0, 6, 0, 0, 0, 3],
    #     [4, 0, 0, 8, 0, 3, 0, 0, 1],
    #     [7, 0, 0, 0, 2, 0, 0, 0, 6],
    #     [0, 6, 0, 0, 0, 0, 2, 8, 0],
    #     [0, 0, 0, 4, 1, 9, 0, 0, 5],
    #     [0, 0, 0, 0, 8, 0, 0, 7, 9]
    # ]
    # grid = [
    #     [0, 9, 6, 8, 3, 2, 7, 5, 0],
    #     [0, 0, 0, 7, 4, 5, 0, 0, 0],
    #     [0, 5, 3, 0, 9, 0, 0, 8, 0],
    #     [1, 0, 0, 4, 2, 0, 3, 0, 0],
    #     [0, 6, 2, 0, 0, 0, 0, 0, 4],
    #     [3, 7, 0, 0, 0, 0, 8, 0, 9],
    #     [0, 0, 0, 9, 8, 4, 0, 0, 6],
    #     [0, 4, 9, 0, 0, 0, 1, 3, 8],
    #     [0, 0, 7, 0, 1, 3, 0, 0, 5]
    # ]
    grid = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 8, 5, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0]
    ]
    
    print("元の数独:")
    print_grid(grid)
    print("\n解いた後:")
    
    if solve_sudoku(grid):
        print_grid(grid)
    else:
        print("解が見つかりませんでした。")
