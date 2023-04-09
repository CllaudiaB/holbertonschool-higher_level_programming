#!/usr/bin/node

let arg = parseInt(process.argv[2]);

if (arg == null) {
    console.log('Not a number');
} else if (Number.isInteger(arg)) {
    console.log('My number:', arg);
} else {
    console.log('Not a number');
}
