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
  let colors = {"red":0,"green":0,"blue":0};
  let product = 1;

  for (var key in colors) {
    let re = new RegExp(`\\d+\ ${key}`, 'g');
    let biggest = line.match(re).map(function(blocks) {
      return parseInt(blocks.match(/\d+/)[0]);
    }).reduce(max,0);
    colors[key] = biggest;
    product *= biggest;
  }
  return product;
}).reduce(add,0);

console.log(sum);