#!/usr/bin/node

module.exports.callMeMoby = function (a, callback) {
  for (let i = 0; i < a; i++) {
    callback();
  }
};
