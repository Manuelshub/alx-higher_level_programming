#!/usr/bin/node

// fs: file system
const fs = require('fs');
// filename
const filename = process.argv[2];

fs.readFile(filename, 'utf-8', (data, err) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
