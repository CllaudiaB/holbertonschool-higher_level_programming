#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  double () {
    for (let i = 0; i < this.height * 2; i++) {
      console.log('X'.repeat(this.width * 2));
    }
  }

  rotate () {
    for (let i = 0; i < this.width; i++) {
      console.log('X'.repeat(this.height));
    }
  }
}

module.exports = Rectangle;
