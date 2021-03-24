#!/usr/bin/node
// Made by Facundo Diaz to Holberton School 2021

const fs = require('fs');
const firstfile = process.argv[2];
const secondfile = process.argv[3];
const destino = process.argv[4];

const text = fs.readFileSync(firstfile, { encoding: 'utf8', flag: 'r' }, function (err, data) { if (err) { console.log(err); } });
const text2 = fs.readFileSync(secondfile, { encoding: 'utf8', flag: 'r' }, function (err, data) { if (err) { console.log(err); } });
const text3 = text + '\n' + text2 + '\n';
fs.writeFileSync(destino, text3);
