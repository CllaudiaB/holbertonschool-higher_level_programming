#!/usr/bin/node

let arg = process.argv[2];

if (arg == null) {
    console.log('Not a number');
} else if (parseInt(arg) == 89) {
    console.log('My number:' ,Math.trunc(arg));
} else {
    console.log('Not a number');
}
