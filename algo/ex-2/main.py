"""
Contributers:
Ron Megini 318955499
Adi Hakimi 209445121
"""

import random

def get_highest_tower(widths: list, lengths: list, heights: list):
    
    # Convert the list of sorted_blocks dimentions
    blocks = []
    for width, length, height in zip(widths, lengths, heights):
        block = {'width': width, 'length': length, 'height': height}
        blocks.append(block)
    
    blocks_amount = len(blocks)
    highest_towers = [0] * blocks_amount
    prev_block = [None] * blocks_amount

    # Sort sorted_blocks by length
    sorted_blocks = sorted(blocks, key=lambda x: x['length'], reverse=True)

    # First place each block as the base of a tower
    for index in range(blocks_amount):
        highest_towers[index] = sorted_blocks[index]['height']

    # Find the optimal highest_towers values
    for i in range(1, blocks_amount):
        for j in range(0, i):
            # Is it legal to place the box
            if (sorted_blocks[i]['length'] < sorted_blocks[j]['length']
                and sorted_blocks[i]['width'] < sorted_blocks[j]['width']):
                if highest_towers[i] < highest_towers[j] + sorted_blocks[i]['height']:
                    highest_towers[i] = highest_towers[j] + sorted_blocks[i]['height']
                    prev_block[i] = j
    
    # Return max height
    max_height = max(highest_towers)
    start_index = highest_towers.index(max_height)
    print_floors(sorted_blocks, prev_block, start_index)
    
    return max_height


def print_floors(blocks, previous_floors, index):
    current_floor_number = 1
    print("----------------------------------")

    
    # Print each floor
    while previous_floors[index]:
        print_floor(blocks[index], current_floor_number)
        print("----------------------------------")
        index = previous_floors[index]
        current_floor_number += 1

    print_floor(blocks[index], current_floor_number)
    print("----------------------------------")

def print_floor(block, floor_number):
    print(f"Width {block['width']}, Length {block['length']}, Height {block['height']}")

def random_array(length):
    return [random.randint(1, 200) for _ in range(length)]

def random_tower(blocks_amount):
    print(f"{blocks_amount} blocks:")
    height = random_array(blocks_amount)
    width = random_array(blocks_amount)
    length = random_array(blocks_amount)
  
    print(f"The height of the highest tower is {get_highest_tower(width, length, height)}")

random_tower(20)
print("\n")
random_tower(30)
