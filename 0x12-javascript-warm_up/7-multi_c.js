#!/usr/bin/node

/**
 * prints x times 'C is fun'
 */

let arg = process.argv[2];

arg = parseInt(arg);

if (arg) {
  if (arg > 0) {
    for (let i = 0; i < arg; i++) {
      console.log('C is fun');
    }
  }
} else {
  console.log('Missing number of occurrences');
}
