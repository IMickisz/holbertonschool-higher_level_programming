#!/usr/bin/node

const fs = require('fs');
const args = process.argv;
const axios = require('axios').default;

axios.get(args[2])
  .then(function (response) {
    fs.writeFile(args[3], response.data, err => {
      if (err) {
        console.log(err);
      }
    });
  })
  .catch(function (error) {
    console.log(error);
  });
