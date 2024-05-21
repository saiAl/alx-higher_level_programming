#!/usr/bin/node
//  script that gets the contents of a webpage and stores it in a file.

const { argv } = require('node:process');
const request = require('request');
const fs = require('node:fs');

request(argv[2], (err, response, body) => {
  fs.writeFile(argv[3], body, (err) => {
    if (err) { return console.error(err); }
  });
});
