#!/usr/bin/node

/**
 * Rectangle: class that defines a rectangle
 * @width: the width of rect
 * @height: the height of rect
 *
 */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
