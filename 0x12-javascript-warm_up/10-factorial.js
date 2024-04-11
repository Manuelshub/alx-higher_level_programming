#!/usr/bin/node

function fact (num) {
  if (isNaN(num)) {
    return 1;
  } else if (num === 0) {
    return 1;
  } else {
    return num * fact(num - 1);
  }
}

const num = parseInt(process.argv[2], 10);
const factorial = fact(num);
console.log(factorial);
