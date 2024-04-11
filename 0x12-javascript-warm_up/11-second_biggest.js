#!/usr/bin/node

const args = process.argv.slice(2);
if (args.length < 2) {
  console.log('0');
}

const numbers = args.map(Number);
let max = -Infinity;
let secondMax = -Infinity;
for (let i = 0; i < args.length; i++) {
  if (numbers[i] > max) {
    secondMax = max;
    max = numbers[i];
  } else if (numbers[i] > max && numbers[i] !== max) {
    secondMax = numbers[i];
  }
}
if (secondMax === -Infinity) {
	console.log('0');
}
console.log(secondMax);
