#!/usr/bin/node

const { argv } = require('node:process');
const arr = [];

for (let x = 2; x < argv.length; x++) {
  arr.push(argv[x]);
}

const idx = arr.length - 2;
console.log(arr.sort()[idx]);
