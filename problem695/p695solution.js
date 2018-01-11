#!/usr/bin/env node

/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxAreaOfIsland = function(grid) {
  const seen = [];
  let max = 0;
  
  for (let i = 0; i < grid.length; i+= 1) {
      for (let j = 0; j < grid[i].length; j += 1) {
          max = Math.max(max, resolve(grid, seen, i, j));
      }
  }
  return max;
};

function resolve(grid, seen, i, j) {
  if (grid[i] === undefined || grid[i][j] === undefined) {
      return 0;
  }
  if (seen[i * grid[0].length + j] === true) {
      return 0;
  }
  seen[i * grid[0].length + j] = true;
  if (grid[i][j] == 0) {
      return 0;
  }
  return 1
    + resolve(grid, seen, i - 1, j) 
    + resolve(grid, seen, i + 1, j)
    + resolve(grid, seen, i, j - 1)
    + resolve(grid, seen, i, j + 1);
}

islands1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]
islands2 = [[0,0,0,0,0,0,0,0]]
islands3 = [[0,0,0,0,1,0,0,0],
            [0,0,0,0,1,0,0,0]]

console.info(maxAreaOfIsland(islands1));
console.info(maxAreaOfIsland(islands2));
console.info(maxAreaOfIsland(islands3));