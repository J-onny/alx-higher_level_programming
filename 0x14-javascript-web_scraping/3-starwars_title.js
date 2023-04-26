#!/usr/bin/node
const mode = require('request');
const filmID = parseInt(process.argv[2]);
const apiurl = 'https://swapi-api.hbtn.io/api/films/' + filmID;
let data;

mode(apiurl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    data = JSON.parse(body);
    console.log(data.title);
  }
});
