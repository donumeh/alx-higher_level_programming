#!/usr/bin/node

const data = require('./101-data.js');

const occurrencesByUserId = data.dict;

const userIdsByOccurrence = {};

for (const userId in occurrencesByUserId) {
  const occurrences = occurrencesByUserId[userId];

  if (!userIdsByOccurrence[occurrences]) {
    userIdsByOccurrence[occurrences] = [];
  }

  userIdsByOccurrence[occurrences].push(userId);
}

console.log(userIdsByOccurrence);
