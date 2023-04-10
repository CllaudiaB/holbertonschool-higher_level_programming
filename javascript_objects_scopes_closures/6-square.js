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
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
}

class Square extends Rectangle {
    constructor (size) {
	super(size, size);
	this.size = size;
    }
    charPrint (c) {
	for (let i = 0; i < this.size; i++) {
	    if (c == undefined) {
		console.log('X'.repeat(this.size));
	    } else {
		console.log(c.repeat(this.size));
	    }
	}
    }
}

module.exports = Square;
