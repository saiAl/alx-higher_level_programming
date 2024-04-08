#!/usr/bin/node

const { argv } = require('node:process');

function add (a, b) {
  const res = Number(a) + Number(b);
  console.log(res);
}

add(argv[2], argv[3]);
