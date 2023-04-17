#!/usr/bin/node

const axios = require('axios');
axios.get(process.argv[2])
  .then((response) => console.log('code: ' + response.status))
  .catch((error) => console.log('code: ' + error.response.status));
