#!/usr/bin/node

const args = process.argv;
const axios = require('axios').default;
const dict = {};
let i;

axios.get(args[2])
  .then(function (response) {
    for (i = 0; i < response.data.length; i++) {
      if (response.data[i].completed === true) {
        if (dict[response.data[i].userId] === undefined) {
          dict[response.data[i].userId] = 0;
        }
        dict[response.data[i].userId] += 1;
      }
    }
    console.log(dict);
  })
  .catch(function (error) {
    console.log(error);
  });
