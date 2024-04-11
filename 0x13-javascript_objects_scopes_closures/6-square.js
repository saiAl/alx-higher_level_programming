#!/usr/bin/node

const Square = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let valuesArray = [];

    const array = (chr, x, y) => {
      let str = '';
      const arr = [];

      for (let idx = 0; idx < x; idx++) {
        str += `${chr}`;
      }
      for (let idx = 0; idx < y; idx++) {
        arr.push(str);
      }
      return arr;
    };

    if (typeof c !== 'undefined') {
      valuesArray = array(c, this.width, this.height);
    } else {
      valuesArray = array('X', this.width, this.height);
    }

    valuesArray.forEach((value) => {
      console.log(value);
    });
  }
}
module.exports = Square;
