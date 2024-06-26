#!/usr/bin/node

const args = process.argv.slice(2);
if (args.length < 2) {
  console.log('0');
} else {
  const numbers = args.map(Number);
  let max = Math.max(numbers[0], numbers[1]);
  let secondMax = Math.min(numbers[0], numbers[1]);
  for (let i = 2; i < args.length; i++) {
    if (numbers[i] > max) {
      secondMax = max;
      max = numbers[i];
    } else if (numbers[i] > secondMax && numbers[i] !== max) {
      secondMax = numbers[i];
    } else if (max === secondMax && secondMax !== numbers[i]) {
      secondMax = numbers[i];
    }
  }
  console.log(secondMax);
}
