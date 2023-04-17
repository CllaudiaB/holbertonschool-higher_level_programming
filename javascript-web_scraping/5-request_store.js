#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (err, response, body) {
  if (err) {
    console.log('Error:', err);
  } else {
    fs.writeFile(filePath, body, 'utf8', err => {
    });
  }
});
