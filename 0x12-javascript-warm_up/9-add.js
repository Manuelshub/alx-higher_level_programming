#!/usr/bin/node

function add (a, b) {
  const result = a + b;
  return result;
}

const num1 = parseInt(process.argv[2], 10);
const num2 = parseInt(process.argv[3], 10);
const result = add(num1, num2);
console.log(result);
