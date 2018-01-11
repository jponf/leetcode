#!/usr/bin/env node

/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function(rowIndex) {
    const res = new Array(rowIndex + 1).fill(0);
    res[rowIndex] = 1;
    
    for (let i = 1; i <= rowIndex; i += 1) {
        const startAt = rowIndex - i;
        for (let j = startAt; j <= rowIndex - 1; j += 1) {
            res[j] += res[j + 1];
        }
    }
    return res;
};

for (let i = 0; i < 10; i += 1) {
    console.info(getRow(i));
}