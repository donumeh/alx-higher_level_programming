#!/usr/bin/node

/**
 * searches biggest integer in the list of args
 */

const arrLength = process.argv.length;
let arr = [];

if (arrLength === 2 || arrLength === 3) {
  console.log(0);
} else {
  arr = process.argv.slice(2);

  let newHighest = 0; let formerHighest = 0;
  newHighest = arr[0];

  for (const i in arr) {
    if (i > newHighest) {
      formerHighest = newHighest;
      newHighest = i;
    }
  }

  console.log(formerHighest);
}
