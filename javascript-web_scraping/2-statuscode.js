#!/usr/bin/node

require('fetch');
fetch(process.argv[2])
  .then(response => {
      console.log(response.status);
  });