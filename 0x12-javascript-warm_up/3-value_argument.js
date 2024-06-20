#!/usr/bin/node

/**
 * script that prints the first arg passed to it
 */

const cliArgs = process.argv;

if (cliArgs[2]) {
  console.log(cliArgs[2]);
} else {
  console.log('No argument');
}
