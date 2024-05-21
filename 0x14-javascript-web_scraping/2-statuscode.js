#!/usr/bin/node
// script that display the status code of a GET request.

const request = require('request');
const { argv } = require('node:process');

request(argv[2], (err, res) => {
  if (err) { return console.error(err); }
  console.log(`code: ${res.statusCode}`);
});
