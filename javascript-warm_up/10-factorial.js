#!/usr/bin/node

function fact (number) {
    if (isNaN(number)) {
	return 1;
    } else {
	return number * fact(number - 1);
    }
}

let arg = process.argv;
let result = fact(arg[2]);
console.log(result);
