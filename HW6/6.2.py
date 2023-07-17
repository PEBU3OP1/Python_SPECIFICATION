import random


def check_queen(desk: list) -> bool:
    for i in range(len(desk)):
        for j in range(i + 1, len(desk)):
            if desk[i][0] == desk[j][0] or desk[i][1] == desk[j][1] or \
                    abs(desk[i][0] - desk[j][0]) == abs(desk[i][1] - desk[j][1]):
                return False
    return True


# queens = [[0,1],[1,3],[2,5],[3,7],[4,2],[5,0],[6,6],[7,4]]
queens = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

while not check_queen(queens):

    for i in range(len(queens)):
        for j in range(0, 2):
            queens[i][j] = random.randint(0, 7)



print(queens)