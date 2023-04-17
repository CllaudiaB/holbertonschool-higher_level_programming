#!/usr/bin/node

const fs = require('fs');
const data = 'Python is cool';
fs.writeFile(process.argv[2], data, (err) => {
  if (err) throw err;
  else console.log(data);
});
