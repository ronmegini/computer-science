M_example = [[1,0,1,0,1,1,0,0,1],[1,1,1,1,0,1,1,1,1],[0,1,1,1,0,1,0,0,1],[0,1,1,0,1,1,1,0,0],[1,0,1,1,0,1,1,0,1],[1,1,0,1,0,0,1,0,1],[0,1,1,1,1,1,1,1,1],[1,1,0,1,0,1,0,0,1],[0,0,0,1,1,1,0,0,1]]


def BigCross2(M, m):
    """
    Params:
    M - matrix
    m - matrix size (m*m)
    
    Action:
    Scan the matrix once and map neighbors, eventually return the cross center with the largest neighbors count.

    Return:
    centercross location and leaf_size
    """
    neighbors_matrix = [[[] for x in range(m)] for y in range(m)]
    for row in range(0, m):
        for columeume in range(0, m):
            neighbors_matrix[row][columeume] = [0, 0, 0, 0]
    cross_center = [0, 0]
    leaf_size = 0
    # find up and left values
    for row in range(0, m):
        for columeume in range(0, m):
            if M[row][columeume] == 0:
                neighbors_matrix[row][columeume] = [0, 0, 0, 0]
            else:
                neighbors_matrix[row][columeume] = find_neighbors(M, m, row, columeume)
                neighbors_matrix[row][columeume] = sum_direction(neighbors_matrix, m, (row, columeume), neighbors_matrix[row][columeume])
                #neighbors_matrix[row][columeume] = sum_direction(neighbors_matrix, m, "up",
                #                                      (row - 1, columeume), neighbors_matrix[row][columeume])
                #neighbors_matrix[row][columeume] = sum_direction(neighbors_matrix, m, "left",
                #                                      (row, columeume - 1), neighbors_matrix[row][columeume])
                #neighbors_matrix[row][columeume] = sum_direction(neighbors_matrix, m, "down",
                #                                      (row + 1, columeume), neighbors_matrix[row][columeume])
                #neighbors_matrix[row][columeume] = sum_direction(neighbors_matrix, m, "right",
                #                                      (row, columeume + 1), neighbors_matrix[row][columeume])
    """
    for row in range(m - 1, -1, -1):
        for columeume in range(m - 1, -1, -1):
            if M[row][columeume] == 0:
                neighbors_matrix[row][columeume] = [0, 0, 0, 0]
            else:
                neighbors_matrix[row][columeume] = sum_direction(neighbors_matrix, m, "down",
                                                      (row + 1, columeume), neighbors_matrix[row][columeume])
                neighbors_matrix[row][columeume] = sum_direction(neighbors_matrix, m, "right",
                                                      (row, columeume + 1), neighbors_matrix[row][columeume])
    """
    # find the largest cross
    for row in range(0, m):
        for columeume in range(0, m):
            if check_even(neighbors_matrix, row, columeume) > leaf_size:
                cross_center = [row + 1, columeume + 1]
                leaf_size = check_even(neighbors_matrix, row, columeume)
    if leaf_size > 0:
        return cross_center, leaf_size 
    return "No big cross found"


def sum_direction(M, m, coordinate, neighbors):
    addition_list = [0, 0, 0, 0]
    if is_in_range(m, coordinate):
        row, columeume = coordinate
        addition_list = [0,M[row][columeume][0]+M[row+1][columeume][0], M[row][columeume][0]+M[row][columeume-1][0], 0]
        #row, columeume = coordinate
        #if side == "left":
        #    addition_list = [M[row][columeume][0], 0, 0, 0]
        #elif side == "up":
        #    addition_list = [0, M[row][columeume][1], 0, 0]
        #elif side == "right":
        #    addition_list = [0, 0, M[row][columeume][2], 0]
        #elif side == "down":
        #    addition_list = [0, 0, 0, M[row][columeume][3]]

    return list([x + y for x, y in zip(addition_list, neighbors)])




def find_neighbors(M, m, row, columeume):
    up = check_neighbors_value(M, m, row - 1, columeume)
    down = check_neighbors_value(M, m, row + 1, columeume)
    right = check_neighbors_value(M, m, row, columeume + 1)
    left = check_neighbors_value(M, m, row, columeume - 1)

    return [up, down, left, right]


def check_neighbors_value(M, m, row, columeume):
    if is_in_range(m, (row, columeume)):
        if M[row][columeume] == 1:
            return 1
    return 0

def is_in_range(m, coordinate):
    row, columeume = coordinate
    return (0 <= row < m) and (0 <= columeume < m)


def check_even(Matrix, row, columeume):
    minimal = min(Matrix[row][columeume])
    return minimal
    

if __name__ == "__main__":
    M_example = [[1,0,1,0,1,1,0,0,1],[1,1,1,1,0,1,1,1,1],[0,1,1,1,0,1,0,0,1],[0,1,1,0,1,1,1,0,0],[1,0,1,1,0,1,1,0,1],[1,1,0,1,0,0,1,0,1],[0,1,1,1,1,1,1,1,1],[1,1,0,1,0,1,0,0,1],[0,0,0,1,1,1,0,0,1]]
    print(BigCross2(M_example,9))