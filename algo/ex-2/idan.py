#################################
# Idan Kalmanzon      206590671 #
# Doron Kedem Goldman 322710781 #
#################################

import random

class Box:
	def __init__(self, l, w, h):
		self.l = l
		self.w = w
		self.h = h

	def __lt__(self, other):
		return self.l < other.l and self.w < other.w

	def print(self):
		print("[%s, %s, %s]" % (self.l, self.w, self.h))

def generateDimensions(blocks_amount):
    length = random.sample(range(1, 201), blocks_amount)
    width  = random.sample(range(1, 201), blocks_amount)
    height = random.sample(range(1, 201), blocks_amount)

    return length, width, height

def generateBoxes(lengths, widths, heights):
	blocks_amount = len(lengths)
	sorted_blocks = [Box(0, 0, 0) for _ in range(blocks_amount)]

	for i in range(blocks_amount):
		sorted_blocks[i] = Box(lengths[i], widths[i], heights[i])

	return sorted_blocks

def highestStableTower(sorted_blocks):
    blocks_amount = len(sorted_blocks)
    highest_towers = [0] * blocks_amount
    prev_block = [-1] * blocks_amount

    # Sort sorted_blocks by length
    sorted_blocks = sorted(sorted_blocks, key=lambda x: x.l, reverse=True)

    for i in range(blocks_amount):
        highest_towers[i] = sorted_blocks[i].h

    # Find optimal highest_towers values bottom-up
    for i in range(1, blocks_amount):
        for j in range(0, i):
            # Is it legal to place the box
            if (sorted_blocks[i] < sorted_blocks[j]):
                if highest_towers[i] < highest_towers[j] + sorted_blocks[i].h:
                    highest_towers[i] = highest_towers[j] + sorted_blocks[i].h
                    prev_block[i] = j

    # Find the index of the box that contributes to the highest tower
    max_height_index = highest_towers.index(max(highest_towers))
    hst_boxes = []
    while max_height_index != -1:
        hst_boxes.append(sorted_blocks[max_height_index])
        max_height_index = prev_block[max_height_index]

    return hst_boxes[::-1], max(highest_towers)  # Reverse the list to get the sorted_blocks in bottom-to-top order and highest_towers value


if __name__ == "__main__":
    # Generate sorted_blocks
	lengths_20, widths_20, heights_20 = generateDimensions(20)
	lengths_30, widths_30, heights_30 = generateDimensions(30)

	boxes_20 = generateBoxes(lengths_20, widths_20, heights_20)
	boxes_30 = generateBoxes(lengths_30, widths_30, heights_30)

	print("----- blocks_amount=20 - dimensions -----\blocks_amount")
	print("Lengths: " + str(lengths_20))
	print("Widths: "  + str(widths_20))
	print("Heights: " + str(heights_20))

	print("\blocks_amount----- blocks_amount=20 - sorted_blocks -----\blocks_amount")
	for box in boxes_20:
		box.print()

	print("\nHighest Stable Tower: " + str(highestStableTower(boxes_20)[1]) + "\blocks_amount")
	hst_20 = highestStableTower(boxes_20)[0]
	for box in hst_20:
		box.print()

	print("\blocks_amount----- blocks_amount=30 - dimensions -----\blocks_amount")
	print("Lengths: " + str(lengths_30))
	print("Widths: "  + str(widths_30))
	print("Heights: " + str(heights_30))

	print("\blocks_amount----- blocks_amount=30 - sorted_blocks -----\blocks_amount")
	for box in boxes_30:
		box.print()

	print("\nHighest Stable Tower: " + str(highestStableTower(boxes_30)[1]) + "\blocks_amount")
	hst_30 = highestStableTower(boxes_30)[0]
	for box in hst_30:
		box.print()