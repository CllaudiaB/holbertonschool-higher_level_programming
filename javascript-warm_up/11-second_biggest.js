#!/usr/bin/node

const args = process.argv;
let firstBiggest = args[2];
let secondBiggest = args[2];

if (args[2] === null || args[2] === 1) {
  console.log('0');
} else {
  for (let i = 3; i < args.length; i++) {
    if (args[i] > firstBiggest) {
      firstBiggest = args[i];
    }
  }
  for (let j = 3; j < args.length; j++) {
    if (args[j] < firstBiggest && args[j] > secondBiggest) {
      secondBiggest = args[j];
    }
  }
  console.log(secondBiggest);
}
