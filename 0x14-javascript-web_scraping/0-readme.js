#!/usr/bin/node

// script that reads and prints the content of a file.

const fs = require('node:fs');
const { argv } = require('node:process');

fs.readFile(argv[2], (err, data) => {
  if (err) { return console.error(err); }
  console.log(data.toString());
});
