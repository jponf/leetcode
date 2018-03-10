#!/usr/bin/env node

const ll = {
  'I': 1,
  'V': 5,
  'X': 10,
  'L': 50,
  'C': 100,
  'D': 500,
  'M': 1000,
};

/**
* @param {string} s
* @return {number}
*/
var romanToInt = function(s) {
  let max = 0;
  let res = 0;
  for (let i = s.length - 1; i >= 0; i -= 1) {
      const curr = s[i];
      const currVal = ll[curr];
      res += currVal >= max ? currVal : -currVal;
      max = Math.max(max, currVal);
  }
  return res;
};

console.info(romanToInt('I'));
console.info(romanToInt('IV'));
console.info(romanToInt('V'));
console.info(romanToInt('VI'));
console.info(romanToInt('MMMCMXCIX'));
