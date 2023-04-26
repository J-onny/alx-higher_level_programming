#!/usr/bin/node
const mode = require('request');
const apiurl = process.argv[2];

mode(apiurl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
