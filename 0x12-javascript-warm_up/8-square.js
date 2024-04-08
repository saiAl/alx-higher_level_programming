#!/usr/bin/node

const { argv } = require('node:process');
const arr = [];
let axies = '';

if (argv.length < 3 || isNaN(argv[2])) {
  console.log('Missing size');
} else {
  for (let x = 0; x < Number(argv[2]); x++) {
    axies += 'X';
  }

  for (let y = 0; y < Number(argv[2]); y++) {
    arr.push(axies);
  }

  arr.forEach((value) => {
    console.log(value);
  });
}
