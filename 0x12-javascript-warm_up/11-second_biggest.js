#!/usr/bin/node

/**
 * prints the second largest number
 */

let args = process.argv.slice(2).map(Number);

if (args.length === 0 || args.length === 1) {
	console.log(0);
} else {
	let max = Math.max(...args);
	let secondBiggest = Math.max(...args.filter(x => x < max));
	console.log(secondBiggest);
}
