#!/usr/bin/node
// Made by Facundo Diaz to Holberton School 2021
class Rectangle {
  constructor (h, w) {
    if (h > 0 && w > 0) {
      this.width = h;
      this.height = w;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
