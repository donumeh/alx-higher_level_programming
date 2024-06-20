#!/usr/bin/node

/**
 * searches biggest integer in the list of args
 */

const arrLength = process.argv.length;
let arr = [];

if (arrLength === 2 || arrLength === 3) {
  console.log(0);
} else {
  const newIntArr = [];
  arr = process.argv.slice(2);

  for (const i of arr) {
    newIntArr.push(parseInt(i));
  }

  let newHighest = 0; let formerHighest = 0;
  newHighest = newIntArr[0];

  for (const i in newIntArr) {
    if (i > newHighest) {
      formerHighest = newHighest;
      newHighest = i;
    }
  }
  console.log(formerHighest);
}
