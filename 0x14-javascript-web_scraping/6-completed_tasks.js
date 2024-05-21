#!/usr/bin/node
// script that computes the number of tasks completed by user id.

const request = require('request');
const { argv } = require('node:process');

request(argv[2], (err, response, body) => {
  if (err) { return console.log(err); }
  const obj = JSON.parse(body);
  const dict = {};

  for (let x = 0; x < obj.length; x++) {
    const id = String(obj[x].userId);
    dict[id] = 0;
  }

  let number = 0;
  Object.keys(dict).forEach((key) => {
    for (let x = 0; x < obj.length; x++) {
      if (String(obj[x].userId) === key) {
        if (obj[x].completed === true) {
          number++;
        }
      }
    }
    dict[key] = number;
    number = 0;
  });

  console.log(dict);
});
