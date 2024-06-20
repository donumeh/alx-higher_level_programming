#!/usr/bin/node

/**
 * prints a square in CLI
 */

let arg = process.argv[2];

arg = parseInt(arg);

if (arg) {
	if (arg > 0) {

		for (let i = 0; i < arg; i++) {
			for (let y = 0; y < arg; y++) {
				process.stdout.write('X');
			}
			process.stdout.write('\n');
		}
	}
}
else {
	console.log('Missing size');
}
