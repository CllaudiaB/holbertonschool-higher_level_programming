#!/usr/bin/node

const args = process.argv.splice(2);
const list = [];
for (let i = 0; i < args.length; i++) {
  list.push(parseInt(args[i]));
}

let firstBiggest = 1;
let secondBiggest = 1;

if (args.length <= 1) {
  console.log('0');
} else {
  for (let i = 0; i <= list.length; i++) {
    if (list[i] > firstBiggest) {
      firstBiggest = list[i];
    }
  }
  for (let i = 1; i <= list.length; i++) {
    if (secondBiggest < list[i] && list[i] < firstBiggest) {
      secondBiggest = list[i];
    }
  }
  console.log(secondBiggest);
}
