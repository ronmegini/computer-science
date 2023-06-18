const findHighestTower = (w, l, h) => {
    // init blocks array [O(blocks_amount)]
    const blocks = w.map((width, i) => ({
      width,
      len: l[i],
      height: h[i],
    }));
  
    // Sort by base area [O(blocks_amount^2) or O(nlogn)]
    const sortedBlocks = [...blocks].sort(
      (a, b) => a.width * a.len - b.width * b.len
    );
  
    const towerHeights = Array.from({ length: sortedBlocks.length }, () => 0);
    const previousFloors = Array.from({ length: sortedBlocks.length }, () => null);

    // O(blocks_amount^2)
    sortedBlocks.forEach((currBlock, index, allBlocks) => {
      let currMaxHeight = 0;
      let floorAbove = null;
  
      // O(blocks_amount)
      for (let j = index - 1; j >= 0; j--) {
        if (
          currBlock.width > allBlocks[j].width &&
          currBlock.len > allBlocks[j].len &&
          towerHeights[j] > currMaxHeight
        ) {
          currMaxHeight = towerHeights[j];
          floorAbove = j
        }
      }
  
      towerHeights[index] = currMaxHeight + currBlock.height;
      previousFloors[index] = floorAbove
    });
  
    // Return max height [O(blocks_amount)]
    const maxHeight = Math.max(...towerHeights);
    const startIndex = towerHeights.indexOf(maxHeight);

    printTower(sortedBlocks, previousFloors, startIndex);

    return maxHeight;
  };
  
  const printTower = (blocks, previousFloors, index) => {
    let currentFloorNumber = 1;
    console.log("----------------------------------");

    while (previousFloors[index] != null) {
        printFloor(blocks[index], currentFloorNumber);
        console.log("----------------------------------");
        index = previousFloors[index];
        currentFloorNumber++;
    }

    printFloor(blocks[index], currentFloorNumber);
    console.log("----------------------------------");
  }

  const printFloor = (block, floorNumber) => {
        console.log(`Floor ${floorNumber} - Width: ${block.width}, Length: ${block.len}, Height: ${block.height}`);
  }
  const randomArray = (length) =>
    Array.from({ length }, () => Math.floor(Math.random() * 200));
  
  const randomTower = (amountOfBlocks) => {
    console.log(`${amountOfBlocks} blocks:`);
    const height = randomArray(amountOfBlocks);
    const width = randomArray(amountOfBlocks);
    const length = randomArray(amountOfBlocks);
  
    console.log(`The height of the highest tower is ${findHighestTower(width, length, height)}`);
  };
  
  randomTower(20);
  console.log("")
  console.log("");
  randomTower(30);
  