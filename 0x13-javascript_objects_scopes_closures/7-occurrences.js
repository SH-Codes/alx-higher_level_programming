#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let nOccurrences = 0;
  for (const element of list) {
    if (element === searchElement) {
      nOccurrences++;
    }
  }
  return nOccurrences;
};
