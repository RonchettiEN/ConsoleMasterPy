from src.ConsoleMasterPy import ConsoleMaster, exception_handler
import random
from time import sleep

def copy_matrix(matrix):
    return [row[:] for row in matrix]

width, height = 35, 35
console_manager = ConsoleMaster("GAME OF LIFE", 13, width, height)

@exception_handler
def main():
    generation_counter = 0
    
    while True:
        if generation_counter == 0:
            current_matrix = [[0 for x in range(width)] for y in range(height)]
            next_matrix = copy_matrix(current_matrix)
            cell_color = [random.randint(0, 255) for _ in range(3)]

            live_cell_rules = [random.randint(0, 1) for _ in range(9)]
            birth_rules = [random.randint(0, 1) for _ in range(9)]

            for x in range(width):
                next_matrix[x][0] = 0
                next_matrix[x][height - 1] = 0
                next_matrix[x][1] = 1
                next_matrix[x][height - 2] = 1

            for y in range(height):
                next_matrix[0][y] = 0
                next_matrix[width - 1][y] = 0
                next_matrix[1][y] = 1
                next_matrix[width - 2][y] = 1

            for x in range(1, width - 1):
                for y in range(1, height - 1):
                    cell_value = next_matrix[x][y]
                    console_manager.go_xy(x, y)
                    color = cell_color if cell_value else [0, 0, 0]
                    console_manager.print_with_color(color, [0, 0, 0], " ")
            generation_counter = 300

        generation_counter -= 1

        current_matrix = copy_matrix(next_matrix)
        for x in range(1, width - 1):
            for y in range(1, height - 1):
                neighbors = [(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2) if not (i == 0 and j == 0)]
                count = sum(1 for i, j in neighbors if 0 <= i < width and 0 <= j < height and current_matrix[i][j] == 1)

                if current_matrix[x][y] == 1:
                    if not live_cell_rules[count]:
                        next_matrix[x][y] = 0
                        console_manager.go_xy(x, y)
                        console_manager.print_with_color([0, 0, 0], [0, 0, 0], " ")
                    else:
                        next_matrix[x][y] = 1
                else:
                    if birth_rules[count]:
                        next_matrix[x][y] = 1
                        console_manager.go_xy(x, y)
                        console_manager.print_with_color(cell_color, [0, 0, 0], " ")
                    else:
                        next_matrix[x][y] = 0
        sleep(0.05)

main()
