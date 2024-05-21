#!/usr/bin/node
// script that write data into a file

const fs = require('node:fs');
const { argv } = require('node:process');

fs.writeFile(argv[2], argv[3], (err, data) => {
  if (err) { return console.error(err); }
});
