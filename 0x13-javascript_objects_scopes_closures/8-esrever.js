#!/usr/bin/node

exports.esrever = function (list) {
  const len = list.length;
  const revArray = [];
  for (let x = len - 1; x >= 0; --x) {
    revArray.push(list[x]);
  }
  return revArray;
};
