#!/usr/bin/node

const Square2 = require('./5-square');

class Square extends Square2 {
  constructor (size) {
    super(size, size);
      this.size = this.height;
  }

  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      if (c === undefined) {
        console.log('X'.repeat(this.size));
      } else {
        console.log(c.repeat(this.size));
      }
    }
  }
}

module.exports = Square;
