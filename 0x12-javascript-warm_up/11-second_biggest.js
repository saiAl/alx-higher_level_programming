#!/usr/bin/node

const { argv } = require('node:process');
const arr = [];

if (argv.length <= 3) {
  console.log(0);
} else {
  for (let x = 2; x < argv.length; x++) {
    arr.push(Number(argv[x]));
  }

  const idx = arr.length - 2;
  const sortedArr = arr.sort();
  console.log(sortedArr[idx]);
}
