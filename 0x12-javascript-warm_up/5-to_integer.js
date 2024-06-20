#!/usr/bin/node

/**
 * prints "My number: <number>" if it can be
 * converted to int else NaN
 */

let arg = process.argv[2];

arg = parseInt(arg);

if (arg) {
  console.log(`My number: ${arg}`);
} else {
  console.log('Not a number');
}
