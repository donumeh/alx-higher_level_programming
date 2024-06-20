#!/usr/bin/node

/**
 * script that computes and prints a factorial
 */

const arg = parseInt(process.argv[2]);

function factorial (num) {
  if (isNaN(arg)) {
    return (1);
  }
  if (num === 1) { return (1); }
  return (num * factorial(num - 1));
}

const fact = factorial(arg);
console.log(fact);
