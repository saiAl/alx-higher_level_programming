#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};

Object.entries(dict).forEach(([k, v]) => {
  if (!newDict[v]) {
    newDict[v] = [];
  }
  newDict[v].push(k);
});
