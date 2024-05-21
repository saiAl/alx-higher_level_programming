#!/usr/bin/node
//  script that prints the title of a Star Wars
//    movie where the episode number matches a given integer.

const { argv } = require('node:process');
const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${argv[2]}`, (err, response, body) => {
  if (err) { return console.error(err); }
  const obj = JSON.parse(body);
  console.log(obj.title);
});
