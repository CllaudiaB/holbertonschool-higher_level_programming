#!/usr/bin/node

const request = require('request');
let count = 0;

request({
  url: 'https://swapi-api.hbtn.io/api/films/',
  json: true
}, (err, response, body) => {
  if (err) {
    console.log('Error:', err);
  }
  const result = body.results;
  for (let i = 0; i < result.length; i++) {
    const character = result[i].characters;
    for (let j = 0; j < character.length; j++) {
      if (character[j].search('18') > 0) {
        count += 1;
      }
    }
  }
  console.log(count);
});
