#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

request({
  url: 'https://swapi-api.hbtn.io/api/films/${id}',
  json: true
}, (err, response, body) => {
  if (err) {
    console.log('Error:' + err);
  }
  console.log(body.title);
});
