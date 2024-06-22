#!/usr/bin/node

const SquareX = require('./5-square');

/**
 * Square: defines a square
 */

class Square extends SquareX {
  /* constructor (size) {
    super(size);
  } */

  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      for (let y = 0; y < this.width; y++) {
        process.stdout.write(c);
      }
      console.log();
    }
  }
}

module.exports = Square;
