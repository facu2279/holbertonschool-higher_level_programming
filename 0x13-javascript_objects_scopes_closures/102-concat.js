#!/usr/bin/node
// xdxd
const fs = require('fs');
const first = process.argv[2];
const second = process.argv[3];
const path = process.argv[4];
// xdxd
let alltext = fs.readFileSync(first,
  { encoding: 'utf8', flag: 'r' },
  function (err, data) {
    if (err) { console.log(err); }
  });
// xdxd
alltext += fs.readFileSync(second,
  { encoding: 'utf8', flag: 'r' },
  function (err, data) {
    if (err) { console.log(err); }
  });
// xdxd
fs.writeFileSync(path, alltext);
