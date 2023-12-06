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

var sum = input.map(function(line) {
  line = line.replace(/\D/g,'');
  return parseInt(line[0]+line.slice(-1));
}).reduce(add,0);

console.log(sum);