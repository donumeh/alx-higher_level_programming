#!/usr/bin/node

/**
 * Rectangle: defines a rectangle
 * @width: the width of the rect
 * @height: the height of the rect
 *
 */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let y = 0; y < this.width; y++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

/**
 * Square: defines a square and inherits from Rectangle
 * @size: size of the square
 */

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
