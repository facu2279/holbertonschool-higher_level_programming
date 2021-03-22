#!/usr/bin/node
const argv = process.argv;
fact(parseInt(argv[2]));

function fact (a) {
  if (isNaN(a)) {
    console.log('1');
  } else {
    console.log(a * a);
  }
}
