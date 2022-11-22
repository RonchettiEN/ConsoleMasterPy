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
            colour = [
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            ]

            live_laws = [
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
            ]
            born_laws = [
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
                random.randint(0, 1),
            ]

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
                    if now_matrix[x][y] == 1:
                        cm.go_xy(x, y)
                        cm.print_with_color(colour, [0, 0, 0], " ")
                    else:
                        cm.go_xy(x, y)
                        cm.print_with_color([0, 0, 0], [0, 0, 0], " ")
            counter = 300
        counter -= 1

        pass_matrix = copy_matrix(now_matrix)
        for x in range(1, w - 1):
            for y in range(1, h - 1):
                count = 0
                if x >= 0 and y >= 0 and pass_matrix[x - 1][y - 1] == 1:
                    count += 1
                if y >= 0 and pass_matrix[x][y - 1] == 1:
                    count += 1
                if x <= w and y >= 0 and pass_matrix[x + 1][y - 1] == 1:
                    count += 1
                if x >= 0 and pass_matrix[x - 1][y] == 1:
                    count += 1
                if x <= w and pass_matrix[x + 1][y] == 1:
                    count += 1
                if x >= 0 and y <= h and pass_matrix[x - 1][y + 1] == 1:
                    count += 1
                if y <= h and pass_matrix[x][y + 1] == 1:
                    count += 1
                if x <= w and y <= h and pass_matrix[x + 1][y + 1] == 1:
                    count += 1

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
