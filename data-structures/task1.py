"""
Authers:
Ron Megini - 318955499
Noy Krief - 206943045
"""

from numpy import random


def BigCross1(M,m):
    """
    Param: M - metrix, m - size
    Search for the cross center and scan up, down, right and left to find the size

    Complications:
    F(n) = F(n) {loop over all the matrix} + f(0.5n) {Worstly scan half of the matrix to find the cross}
    O(n) = O(n^1.5)
    """
    #counters
    cross_center = [0,0]
    leaf_size = 0
    for row in range(m):
        for columeumeume in range(m):
            i = 1
            if M[row][columeumeume] == 1:
                while True:
                    # if the leaf_size reached the maximun size
                    if m+row == i or m-row == i or m+columeumeume == i or m-columeumeume == i:
                        if i > leaf_size:
                            leaf_size=i
                            cross_center = [row,columeumeume]
                        break
                    # check if the cross's condition met, if so increase i by 1
                    elif M[row+i][columeumeume] == M[row-i][columeumeume] == M[row][columeumeume+i] == M[row][columeumeume-i] == 1:
                        i = i + 1
                    # if condition doesn't met, check if new record reached, record and exit
                    else:
                        if i > leaf_size:
                            leaf_size=i
                            cross_center = [row,columeumeume]
                        break
    cross_center = [cross_center[0]+1, cross_center[1]+1]
    return(cross_center,leaf_size-1)
            

def random_matrix(size):
    #matrix = random.randint(2, size=(size, size))
    matrix = [[random.randint(0, 2) for x in range(size)] for y in range(size)]
    return matrix

def print_matrix(M,m):
    for row in range(m):
        print(M[row])


if __name__ == "__main__":
    
    M_example = [[1,0,1,0,1,1,0,0,1],[1,1,1,1,0,1,1,1,1],[0,1,1,1,0,1,0,0,1],[0,1,1,0,1,1,1,0,0],[1,0,1,1,0,1,1,0,1],[1,1,0,1,0,0,1,0,1],[0,1,1,1,1,1,1,1,1],[1,1,0,1,0,1,0,0,1],[0,0,0,1,1,1,0,0,1]]
    M15 = random_matrix(15)
    M50 = random_matrix(50)

    # Example from explanation
    print("Example matrix:")
    print_matrix(M_example,9)
    print("Crosscenter and leaf of the largest cross: {}".format(BigCross1(M_example,9)))
    
    # Matrix 15*15
    print("Matrix 15*15:")
    print_matrix(M15,15)
    print("Crosscenter and leaf of the largest cross: {}".format(BigCross1(M15,15)))


    # Matrix 50*50
    print("Matrix 50*50:")
    print_matrix(M50,50)
    print("Crosscenter and leaf of the largest cross: {}".format(BigCross1(M50,50)))
