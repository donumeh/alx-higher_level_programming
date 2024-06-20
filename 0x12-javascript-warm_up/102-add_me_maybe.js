#!/usr/bin/node
module.exports.addMeMaybe = function (a, callback) {
  const result = a + 1;
  callback(result);
};
