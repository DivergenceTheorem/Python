from random import randint
from sys import argv

NUMBER_OF_QUEENS = 8
BOARD_DIMENSION = 8
# board: list[list[int]] = [[x+1 for x in range(BOARD_DIMENSION)] for _ in range(BOARD_DIMENSION)]

def assign_figures(dimension: int, queens: int) -> list[tuple[int, int]]: # Рандомно расстанавливает ферзей на доске
    count = 0
    positions = []
    while (count < queens):
        position = (randint(0, dimension - 1), randint(0, dimension - 1))
        if (position not in positions):
            count += 1
            positions.append(position)

    return positions

# print(positions)

def is_attacking(positions: list[tuple[int, int]], dimension: int) -> bool: # Функция проверяет, есть ли среди ферзей хотя бы один случай, когда один атакует другого
    attacked_pos: list[list[int]] = [[0 for _ in range(dimension)] for _ in range(dimension)]
    for item in positions:
        x, y = item[0], item[1]
        # print(f"({x}, {y})")
        for i in range(dimension):
            if(attacked_pos[x][i] != '*'):
                attacked_pos[x][i] = 1
            else:
                attacked_pos[x][i] = 'X'
                return False

            if(attacked_pos[i][y] != '*'):
                attacked_pos[i][y] = 1
            else: 
                attacked_pos[i][y] = 'X'
                return False
            

        for i in range(x+1):
            if(y-i >= 0):
                if(attacked_pos[x-i][y-i] == '*'):
                    attacked_pos[x-i][y-i] = 'X'
                    return False
                else:
                    attacked_pos[x-i][y-i] = 1

            if(y+i <= dimension - 1):
                if(attacked_pos[x-i][y+i] == '*'):
                    attacked_pos[x-i][y+i] = 'X'
                    return False
                else:
                    attacked_pos[x-i][y+i] = 1

        for i in range(x+1, dimension):
            if(y - (i - x)>= 0):
                attacked_pos[i][y - (i - x)] = 1
            if(y + (i - x)<= dimension - 1):
                attacked_pos[i][y + (i - x)] = 1

        attacked_pos[x][y] = '*'


    # for i in attacked_pos:
    #     # print(i)
    #     for index, j in enumerate(i):
    #         if(index != BOARD_DIMENSION - 1):
    #             print(j, end = ' ')
    #         else:
    #             print(j, end = '')
    #     print()


    return True

def display_positions(dimension, queens):
    positions = assign_figures(dimension, queens)
    for pos in range(4):
        print(f"Position {pos + 1}:  [", end = '')
        positions = assign_figures(dimension, queens)
        while(is_attacking(positions, dimension) != True):
            positions = assign_figures(dimension, queens)
        
        for index, i in enumerate(positions):
            if(index < len(positions) - 1):
                print('(', i[0], ", ", i[1], ")", end = " | ")
            else:
                print('(', i[0], ", ", i[1], ")", end = "")

        print("]")

# for i in is_attacking(board, positions):
#     print(i, end = '\n')
    


