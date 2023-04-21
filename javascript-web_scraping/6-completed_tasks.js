#!/usr/bin/node

const request = require('request');
let myDict = {};

request({
  url: process.argv[2],
  json: true
}, (err, response, body) => {
  if (err) {
    console.log('Error:', err);
  }
for (let i = 0; i < body.length; i++) {
    if (body[i].completed == true) {
      if (myDict[body[i].userId] === undefined) {
        myDict[body[i].userId] = 0;
      }
      myDict[body[i].userId] += 1;
    }
}
console.log(myDict);
});
