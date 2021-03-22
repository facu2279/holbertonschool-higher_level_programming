#!/usr/bin/node
let i = 0;
process.argv.forEach((val, index) => {
  i++;
});
if (i < 3) {
  console.log('undefined is undefined');
} else {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
