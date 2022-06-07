#!/usr/bin/node

const args = process.argv;
const axios = require('axios').default;
let count = 0;
let i;
let j;

axios.get(args[2])
  .then(function (response) {
    for (i = 0; i < response.data.results.length; i++) {
      for (j = 0; j < response.data.results[i].characters.length; j++) {
        if (response.data.results[i].characters[j].includes(18) === true) {
          count += 1;
        }
      }
    }
    console.log(count);
  })
  .catch(function (error) {
    console.log(error);
  });
