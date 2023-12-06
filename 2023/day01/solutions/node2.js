const path = require('path');
const fs = require('fs');

const input = fs
	.readFileSync('../input.txt', 'utf8')
	.toString()
	.trim()
	.split('\n');

function add(num, oldSum) {
  return num + oldSum;
}
function rev(str) {
  return str.split("").reverse().join("");
}

nums = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9
}
let cnt = 0;
var sum = input.map(function(line) {
  lineF = line.replace(/one|two|three|four|five|six|seven|eight|nine/gi, m => nums[m]);
  lineB = rev(line).replace(/enin|thgie|neves|xis|evif|ruof|eerht|owt|eno/gi, m => nums[rev(m)]);
  lineF = lineF.replace(/\D/g,'');
  lineB = lineB.replace(/\D/g,'');
  return parseInt(lineF[0]+lineB[0]);
}).reduce(add,0);

console.log(sum);