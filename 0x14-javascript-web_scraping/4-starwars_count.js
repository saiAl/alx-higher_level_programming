#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present.

const { argv } = require('node:process');
const request = require('request');

const id = 18;

request(argv[2], (err, response, body) => {
  if (err) { return console.error(err); }
  const obj = JSON.parse(body);
  let number = 0;
  const reg = /\d+/;
  for (let x = 0; x < obj.results.length; x++) {
    const array = obj.results[x].characters;
    array.forEach((str) => {
      if (str.match(reg) === id) { number++; }
    });
  }

  console.log(number);
});
