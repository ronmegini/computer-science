import random

def get_highest_tower(w, l, h):

    # Create blocks array with dimensions
    blocks = []
    for width, length, height in zip(w, l, h):
        block = {'width': width, 'len': length, 'height': height}
        blocks.append(block)

    # O(blocks_amount^2)
    # Sort the blocks by the base area
    sorted_blocks = sorted(blocks, key=lambda block: block['width'] * block['len'])

    # Init lists of zeros and nulls in the length of the sorted blocks array
    # Later we will save the data into those lists as part of the dynamic programing technic
    tower_heights = [0] * len(sorted_blocks)
    previous_floors = [None] * len(sorted_blocks)

    # O(blocks_amount^2)
    # Get the block and the index of it
    for current_location, current_block in enumerate(sorted_blocks):
        current_max_height = 0
        floor_above = None

        # Iterates from current_location - 1 down to 0
        print("--------------------------------------")
        for location in range(current_location - 1, -1, -1):
            print(sorted_blocks[location])
            # Check if the block is legal (base smaller than the previous)
            if (
                current_block['width'] > sorted_blocks[location]['width'] and
                current_block['len'] > sorted_blocks[location]['len'] and
                tower_heights[location] > current_max_height
            ):
                current_max_height = tower_heights[location]
                print(current_max_height)
                print(tower_heights)
                floor_above = location

        # Save the result for later usage (dynamic programming)
        tower_heights[current_location] = current_max_height + current_block['height']
        previous_floors[current_location] = floor_above
  
    # Return max height
    max_height = max(tower_heights)
    start_index = tower_heights.index(max_height)

    print_tower(sorted_blocks, previous_floors, start_index)

    return max_height

def print_tower(blocks, previous_floors, index):
    current_floor_number = 1
    print("----------------------------------")

    while previous_floors[index] is not None:
        print_floor(blocks[index], current_floor_number)
        print("----------------------------------")
        index = previous_floors[index]
        current_floor_number += 1

    print_floor(blocks[index], current_floor_number)
    print("----------------------------------")

def print_floor(block, floor_number):
    print(f"Floor {floor_number}: Width {block['width']}, Length {block['len']}, Height {block['height']}")

def random_array(length):
    return [random.randint(0, 200) for i in range(length)]

def random_tower(blocks_amount):
    print(f"{blocks_amount} blocks:")
    height = random_array(blocks_amount)
    width = random_array(blocks_amount)
    length = random_array(blocks_amount)
  
    print(f"The height of the highest tower is {get_highest_tower(width, length, height)}")

random_tower(20)
print("\blocks_amount")
random_tower(30)
