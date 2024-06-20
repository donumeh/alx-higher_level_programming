#!/usr/bin/node

/**
 * write a script that prints a message
 * depending on CLI args pass
 */

const numOfArgs = process.argv;

if (numOfArgs.length === 3) {
  console.log('Argument found');
} else if (numOfArgs.length > 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
