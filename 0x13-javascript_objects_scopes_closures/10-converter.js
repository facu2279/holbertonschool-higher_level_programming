#!/usr/bin/node
// Made by Facundo Diaz to Holberton School 2021

exports.converter = function (base) {
  function number (a) {
    return (a.toString(base));
  }
  return (number);
};
