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
function max(num, oldMax) {
  return (num > oldMax)?num:oldMax;
}

var sum = input.map(function(line) {
  let id = parseInt(line.match(/\d+/)[0]);
  let colors = {"red":12,"green":13,"blue":14};

  for (var key in colors) {
    let re = new RegExp(`\\d+\ ${key}`, 'g');
    let biggest = line.match(re).map(function(blocks) {
      return parseInt(blocks.match(/\d+/)[0]);
    }).reduce(max,0);
    if(biggest > colors[key]) {
      return 0;
    }
  }
  return id;
}).reduce(add,0);

console.log(sum);