#!/usr/bin/node

const len = parseInt(process.argv[2], 10);
if (!len) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < len; i++) {
    console.log('C is fun');
  }
}
