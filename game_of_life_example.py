from src.ConsoleMasterPy import ConsoleMaster, exception_handler
import random
from time import sleep


def copy_matrix(matrix):
    return [row[:] for row in matrix]


w, h = 35, 35
cm = ConsoleMaster("GAME OF LIFE", 13, w, h)


@exception_handler
def main():

    counter = 0
    while 1:
        if counter == 0:
            pass_matrix = [[0 for x in range(w)] for y in range(h)]
            now_matrix = copy_matrix(pass_matrix)
            colour = [random.randint(0, 255) for i in range(3)]

            live_laws = [random.randint(0, 1) for i in range(9)]
            born_laws = [random.randint(0, 1) for i in range(9)]

            for x in range(w):
                now_matrix[x][0] = 0
                now_matrix[x][h - 1] = 0
                now_matrix[x][1] = 1
                now_matrix[x][h - 2] = 1

            for y in range(h):
                now_matrix[0][y] = 0
                now_matrix[w - 1][y] = 0
                now_matrix[1][y] = 1
                now_matrix[w - 2][y] = 1

            for x in range(1, w - 1):
                for y in range(1, h - 1):
                    value = now_matrix[x][y]
                    cm.go_xy(x, y)
                    color = colour if value else [0, 0, 0]
                    cm.print_with_color(color, [0, 0, 0], " ")
            counter = 300
        counter -= 1

        pass_matrix = copy_matrix(now_matrix)
        for x in range(1, w - 1):
            for y in range(1, h - 1):
                neighbors = [(x + i, y + j) for i in range(-1, 2) for j in range(-1, 2) if not (i == 0 and j == 0)]
                count = sum(1 for i, j in neighbors if 0 <= i <= w and 0 <= j <= h and pass_matrix[i][j] == 1)

                if pass_matrix[x][y] == 1:
                    if not live_laws[count]:
                        now_matrix[x][y] = 0
                        cm.go_xy(x, y)
                        cm.print_with_color([0, 0, 0], [0, 0, 0], " ")
                    else:
                        now_matrix[x][y] = 1
                else:
                    if born_laws[count]:
                        now_matrix[x][y] = 1
                        cm.go_xy(x, y)
                        cm.print_with_color(colour, [0, 0, 0], " ")
                    else:
                        now_matrix[x][y] = 0
        sleep(0.05)


main()
