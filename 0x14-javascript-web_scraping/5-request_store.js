#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const link = process.argv[2];
const nombre = process.argv[3];
request(link, function (err, res, body) {
  if (!err) {
    fs.writeFile(filename, body, 'utf-8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  } else {
        console.error(err);
    });
  }
});
