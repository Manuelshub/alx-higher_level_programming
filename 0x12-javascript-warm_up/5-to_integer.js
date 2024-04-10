#!/usr/bin/node

const myNum = parseInt(process.argv[2], 10);
if (!myNum) {
  console.log('Not a number');
} else {
  console.log('My number:', myNum);
}
