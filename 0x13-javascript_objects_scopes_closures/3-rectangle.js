#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let x = '';
    const arr = [];

    for (let idx = 0; idx < this.width; idx++) {
      x += 'X';
    }
    for (let idy = 0; idy < this.height; idy++) {
      arr.push(x);
    }
    arr.forEach((value) => {
      console.log(value);
    });
  }
}

module.exports = Rectangle;
