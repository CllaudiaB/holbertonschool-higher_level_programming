#!/usr/bin/node

function fact (number) {
  if (!number) {
    return 1;
  } else {
    return number * fact(number - 1);
  }
}

const arg = process.argv;
const result = fact(arg[2]);
console.log(result);
