"""
Authers:
Ron Megini - 318955499
Noy Krief - 206943045
"""

from numpy import random


def BigCross2(M, m):
    """
    Params:
    M - Matrix
    m - matrix size (m*m)
    Description:
    Loop over the matrix once forward and once backward and map the neighbors. Eventually check which cell has the most 1s neighbors.
    Return:
    Cross center location and leaf size
    """
    # Genereate empty matrix which will be used to record neighbors
    neighbors_matrix = [[[0] for x in range(m)] for y in range(m)]
    leaf_size = 0
    cross_center = [0, 0]
    
    # Forward loop over the cells and map the up and left neighbors
    for row in range(m):
        for colume in range(m):
            # If the cross center is 0 in the original matrix, set to 0 the neighbors matrix
            if M[row][colume] == 0:
                neighbors_matrix[row][colume] = [0, 0, 0, 0]
            else:
                # Find the closest neighbors
                neighbors_matrix[row][colume] = closest_neighbors_map(M, m, row, colume)
                # Sum the up neighbors count with the upper cell
                neighbors_matrix[row][colume] = sum_direction(neighbors_matrix, m, "up", (row - 1, colume), neighbors_matrix[row][colume])
                # Sum the left neighbors count with the upper cell
                neighbors_matrix[row][colume] = sum_direction(neighbors_matrix, m, "left", (row, colume - 1), neighbors_matrix[row][colume])
    
    # Backward loop over the cells and map the down and right neighbors
    for row in range(m - 1, -1, -1):
        for colume in range(m - 1, -1, -1):
            # If the cross center is 0 in the original matrix, set to 0 the neighbors matrix
            if M[row][colume] == 0:
                neighbors_matrix[row][colume] = [0, 0, 0, 0]
            else:
                # Sum the up neighbors count with the down cell
                neighbors_matrix[row][colume] = sum_direction(neighbors_matrix, m, "down", (row + 1, colume), neighbors_matrix[row][colume])
                # Sum the up neighbors count with the right cell
                neighbors_matrix[row][colume] = sum_direction(neighbors_matrix, m, "right", (row, colume + 1), neighbors_matrix[row][colume])
    
    # Find the largest cross
    for row in range(0, m):
        for colume in range(0, m):
            if min(neighbors_matrix[row][colume]) > leaf_size:
                cross_center = [row + 1, colume + 1]
                leaf_size = min(neighbors_matrix[row][colume])
    if leaf_size > 0:
        return cross_center, leaf_size
    return "No result"


def sum_direction(M, m, direction, center_location, neighbors):
    """
    Params:
    M - Matrix
    m - matrix size (m*m)
    direction - up/dowm/right/left
    center_location - row and colume
    neighbors - Current cell's neighbors
    Description:
    Summeraize the neighbors of the cells in the selected direction
    Return:
    Cell's neighbors summerized with the other neighbor in the selected direction
    """

    addition_list = [0, 0, 0, 0]
    # If the center_location in range
    row, colume = center_location
    if (0 <= row < m) and (0 <= colume < m):
        row, colume = center_location
        # Sum the direction values to addition_list
        if direction == "up":
            addition_list = [M[row][colume][0], 0, 0, 0]
        elif direction == "down":
            addition_list = [0, M[row][colume][1], 0, 0]
        elif direction == "left":
            addition_list = [0, 0, M[row][colume][2], 0]
        elif direction == "right":
            addition_list = [0, 0, 0, M[row][colume][3]]
    summerized_neighbors = [addition_list[i]+neighbors[i] for i in range(len(addition_list))]
    
    return summerized_neighbors


def closest_neighbors_map(M, m, row, colume):
    """
    Params:
    M - Matrix
    m - matrix size (m*m)
    row - cell's row
    colume - cell's colume
    Description:
    Create neighbors list of the closest neighbors
    Return:
    Neighbors list of the closest neighbors
    """

    up = cell_value(M, m, row - 1, colume)
    down = cell_value(M, m, row + 1, colume)
    left = cell_value(M, m, row, colume - 1)
    right = cell_value(M, m, row, colume + 1)
    return [up, down, left, right]


def cell_value(M, m, row, colume):
    """
    Params:
    M - Matrix
    m - matrix size (m*m)
    row - cell's row
    colume - cell's colume
    Description:
    Check if cell in range and retuen the value
    Return:
    Cell's value
    """

    # Check if cell in range
    if (0 <= row < m) and (0 <= colume < m):
        # return 1 if value 1
        if M[row][colume] == 1:
            return 1
        #return 0 if value 0
        elif M[row][colume] == 0: 
            return 0
    else:
        return 0

def random_matrix(size):
    #matrix = random.randint(2, size=(size, size))
    matrix = [[random.randint(0, 2) for x in range(size)] for y in range(size)]
    return matrix

def print_matrix(M,m):
    for row in range(m):
        print(M[row])

if __name__ == '__main__':
    
    M_example = [[1,0,1,0,1,1,0,0,1],[1,1,1,1,0,1,1,1,1],[0,1,1,1,0,1,0,0,1],[0,1,1,0,1,1,1,0,0],[1,0,1,1,0,1,1,0,1],[1,1,0,1,0,0,1,0,1],[0,1,1,1,1,1,1,1,1],[1,1,0,1,0,1,0,0,1],[0,0,0,1,1,1,0,0,1]]
    M15 = random_matrix(15)
    M50 = random_matrix(50)

    # Example from explanation
    print("Example matrix:")
    print_matrix(M_example,9)
    print("Crosscenter and leaf of the largest cross: {}".format(BigCross2(M_example,9)))
    
    # Matrix 15*15
    print("Matrix 15*15:")
    print_matrix(M15,15)
    print("Crosscenter and leaf of the largest cross: {}".format(BigCross2(M15,15)))


    # Matrix 50*50
    print("Matrix 50*50:")
    print_matrix(M50,50)
    print("Crosscenter and leaf of the largest cross: {}".format(BigCross2(M50,50)))
    
