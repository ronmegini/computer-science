"""
Authers:
Ron Megini - 318955499
Noy Krief - 206943045
"""


class Node:
    """
    Properties:
    data - stack node data
    next - pointer to the nest node, default null
    """
    
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """
    Properties:
    default - null
    head - point to the top node, added by function (The head points to the other nodes in linked list)

    Methodes:
    isEmpty - If stack is empty (True/False)
    push - Add new node to the top
    pop - Remove top node and return value
    top - Read top node

    Diagram:
    newnode -> node1 -> node2 -> node3 
    ^
    head
    """

    def __init__(self):
        self.head = None
 
    def isempty(self):
        """
            Checks if stack is empty
        """
        if self.head == None:
            return True
        else:
            return False
 
    
    def push(self, data):
        """
            Method to add data to the stack
            Adds to the start of the stack
        """
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
 
    def pop(self):
        """
            Remove element that is the current head (start of the stack)
        """
        if self.isempty():
            return None
        else:
            # Removes the head node and makes
            # the preceding one the new head
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data
 
    def top(self):
        """
            Returns the head node data
        """
        if self.isempty():
            return None
        else:
            return self.head.data

    def display(self):
        """
            Prints out the stack
        """
        iternode = self.head
        if self.isempty():
            pass
        else:
            while(iternode != None):
                print(iternode.data, "<-", end=" ")
                iternode = iternode.next
            return   


def valid_location(maze, row, col, n):
    """
    Params:
    maze - maze two dementions array
    row - row location
    col - col location
    n - maze size
    """
    # If in arrays' scope
    if row >= 0 and row <= n-1 and col >= 0 and col <= n-1:
        # If allowed place (0)
        if maze[row][col] == 0:
            return True
    else:
        return False


def solve_maze(maze, n):
    """
    Get maze (two dimension array) containes 0's and 1's.
    The player is able to walk through 0's but cant through 1's.
    Start at (0,0) and finish at (n,n).
    """
    # Creates new stack with the class we created
    stack = Stack()
    # Add the entry point (as a tuple)
    row, col= (0,0)
    stack.push(( row,col))
    # While stack is not empty and we are not in the finish point
    while not stack.isempty() and (row,col) != (n-1,n-1):
        row, col = stack.top()
        maze[row][col] = "X"
        # right
        if valid_location(maze, row, col+1, n):
            stack.push((row, col+1))
        # down
        elif valid_location(maze, row+1, col, n):
            stack.push((row+1, col))
        # left
        elif valid_location(maze, row, col-1, n):
            stack.push((row, col-1))
        # up
        elif valid_location(maze, row-1, col, n):
            stack.push((row-1, col))
        # If no way found, step back
        else:
            stack.pop()
    # Remove the last unrelevent cell
    stack.pop()
    return stack

def print_maze(stack, maze, n):
    """
    Description:
    Print the maze's stack and route solution
    Params:
    stack - stack solution
    maze - maze two dementions array
    n - arrays' size
    """
    print("Maze steps according to the algoritem is:")
    stack.display()
    print("")
    print("Maze route is (♥ is the route):")
    while not stack.isempty():
        col,row = stack.pop()
        maze[col][row] = "♥"
    for row in range(n):
        print("")
        for col in range(n):
            print(maze[row][col], end =" ")
    print("")
    
# Driver code
if __name__ == "__main__":
    MyStack = Stack()
    maze_15 = [[0,0,0,1,0,1,0,0,0,0,0,1,0,0,0],[0,0,0,1,0,1,0,0,0,0,0,1,0,1,1],[0,0,0,1,0,1,0,0,1,1,1,0,0,1,0],[0,0,0,1,0,0,1,0,0,0,1,0,0,1,0],[0,0,0,0,0,0,1,0,0,0,1,0,0,1,0],[0,0,0,0,0,0,1,0,0,0,1,0,0,1,0],[0,0,0,0,0,0,1,0,0,0,0,0,1,1,0],[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],[0,1,0,0,1,0,0,1,0,0,0,0,0,0,0],[0,1,1,0,0,0,0,1,0,0,0,1,0,0,0],[0,0,0,0,0,0,1,0,0,0,1,1,0,0,0],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0],[1,1,0,1,0,0,0,0,1,0,0,0,0,1,0],[0,0,0,1,0,0,0,0,1,0,0,0,0,0,0],[0,0,1,0,0,1,0,0,1,0,0,1,0,0,0]]
    maze_25 = [[0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0],[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0]]
    
    # Show maze solution for the example in the exercise (♥ - final route, X - already visited cell)
    print_maze(solve_maze(maze_15, 15),maze_15,15)
    # Show maze solution for 25*25 self genereted mastrix in the exercise (♥ - final route, X - already visited cell)
    print_maze(solve_maze(maze_25, 25),maze_25,25)
