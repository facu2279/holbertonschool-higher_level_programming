#!/usr/bin/node

// Made by Facundo Diaz to Holberton School 2021
let i = 0;

exports.logMe = function (item) {
  console.log(i + ': ' + item);
  i++;
};
