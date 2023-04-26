#!/usr/bin/node
const mode = require('fs');
const rfile = process.argv[2];
const wtext = process.argv[3];

mode.writeFile(rfile, wtext, 'utf8', function (error, data) {
  if (error) {
    console.log(error);
  }
});
