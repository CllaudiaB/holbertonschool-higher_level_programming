#!/usr/bin/node

const request = require('request');
const arg = process.argv[2];

request(String(arg))
  .on('response', function (response) {
    console.log('code: ' + response.statusCode);
  })
  .on('error', function (err) {
    console.log('code: ', err);
  });
