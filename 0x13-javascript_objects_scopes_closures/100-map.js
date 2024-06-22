#!/usr/bin/node

/**
 * imports an array and computes a new array
 */

const data = require('./100-data');
const list = data.list;
const newList = list.map((num, index) => num * index);

console.log(list);
console.log(newList);
